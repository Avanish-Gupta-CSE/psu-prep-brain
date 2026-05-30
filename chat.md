## Bug 862732 — DMS UI User Access Report (cost center + user status + username)

**Goal**: Make the “DMS UI User Details / User Access Report” accurately reflect:
- **Merged IR cost centers** going forward:
  - **SER402 (US)** should replace legacy **SER400 / SER401**
  - **INS402 (HYD)** should replace legacy **INS400 / INS401**
- **Disabled users** should not appear on the report
- **Active users with access** should appear even if they never logged in (with `last_login_date` empty)
- **Username** should match Keycloak (avoid stale/incorrect `user_name`)

---

### What generates the report (dmsui-api)

- **Report generator**: `dmsui-api-nodejs-polarisplatform/src/services/user-access-report-service.ts`
  - Query base table: `user_details as ud`
  - Join: `leftJoin('user_personas as up', 'ud.user_name', 'up.user_name')`
  - Output uses:
    - `ud.email_id`, `ud.full_name`, `ud.department`, `ud.user_name`, `ud.cost_center`, `ud.job_title`, `ud.last_login_date`, ...
    - Persona fields from `user_personas` (`up.persona`, `up.persona_display_name`)
- **Route**: `dmsui-api-nodejs-polarisplatform/src/routes/reports.ts`
  - `GET /reports/process-user-access-report/:isAutomatedRun`
- **Scheduler** (K8s): `dmsui-api-nodejs-polarisplatform/k8s/qc/cronjob.yaml`
  - `dmsui-api-user-access-report-processor` calls `/reports/process-user-access-report/true`

**Important behavior**:
- Anything missing/stale in **Postgres** (`user_details`, `user_personas`) will appear missing/stale in the report because the generator does not call Keycloak.

---

### Files to open in parallel (validation / walkthrough)

**dmsui-api-nodejs-polarisplatform**
- `dmsui-api-nodejs-polarisplatform/src/services/user-access-report-service.ts` (report query + Excel output)
- `dmsui-api-nodejs-polarisplatform/src/routes/reports.ts` (route: `/reports/process-user-access-report/:isAutomatedRun`)
- `dmsui-api-nodejs-polarisplatform/k8s/qc/cronjob.yaml` (scheduled report processor)
- `dmsui-api-nodejs-polarisplatform/src/routes/track-login.ts` (login tracking endpoint)
- `dmsui-api-nodejs-polarisplatform/src/services/authTrackingService.ts` (`last_login_date` update behavior)
- `dmsui-api-nodejs-polarisplatform/src/constants/excel-column-configs.ts` (User Access Report column list)
- `dmsui-api-nodejs-polarisplatform/src/db/postgres/knexfile.ts` (DB connection wiring)

**dmsuiusermanager-nodejs-polarisplatform**
- `dmsuiusermanager-nodejs-polarisplatform/server.js` (`/api/applypersonas` → DB sync after FGA write)
- `dmsuiusermanager-nodejs-polarisplatform/src/services/UserManagementService.js` (upsert logic for `user_details` + `user_personas`)
- `dmsuiusermanager-nodejs-polarisplatform/src/services/keycloak.js` (Keycloak batch fetch + attribute parsing)
- `dmsuiusermanager-nodejs-polarisplatform/src/utils/personaMatcher.js` (persona derivation from tuples; used for full sync)
- `dmsuiusermanager-nodejs-polarisplatform/src/utils/personaNameMapper.js` (persona → display name mapping)
- `dmsuiusermanager-nodejs-polarisplatform/src/db/postgress/migrations/20250115001_create_user_details_table.js` (table schema + NOT NULLs)
- `dmsuiusermanager-nodejs-polarisplatform/src/db/postgress/migrations/20250115002_create_user_personas_table.js` (table schema)
- `dmsuiusermanager-nodejs-polarisplatform/src/db/postgress/migrations/20251125001_update_user_personas_table.js` (adds `persona_display_name`)
- `dmsuiusermanager-nodejs-polarisplatform/src/db/knexfile.js` (DB connection wiring)

**Avoid in manager walkthrough** (may include secrets):
- `.env*`, `env.*`, `k8s/**/secrets.yaml`

---

### Where `last_login_date` comes from (dmsui-api)

- `dmsui-api-nodejs-polarisplatform/src/routes/track-login.ts` → `AuthTrackingService.trackUserLogin`
- `dmsui-api-nodejs-polarisplatform/src/services/authTrackingService.ts`
  - Updates `user_details.last_login_date` **only if** a `user_details` row already exists for the `user_guid`
  - Does **not** insert a new `user_details` row on login

Implication:
- Users who have access but never logged in should still exist in `user_details` (inserted via user-manager sync) and have `last_login_date = NULL`.

---

### The DB tables live in dmsuiusermanager (schema)

Migrations:
- `dmsuiusermanager-nodejs-polarisplatform/src/db/postgress/migrations/20250115001_create_user_details_table.js`
  - `user_details` columns: `user_guid`, `email_id`, `user_name`, `full_name`, `department`, `cost_center`, `job_title`, `last_login_date`, …
  - Uniques: `user_guid`, `email_id`, `user_name`
- `dmsuiusermanager-nodejs-polarisplatform/src/db/postgress/migrations/20250115002_create_user_personas_table.js`
  - `user_personas` columns: `user_name`, `user_guid`, `persona`, …
- `dmsuiusermanager-nodejs-polarisplatform/src/db/postgress/migrations/20251125001_update_user_personas_table.js`
  - Adds `persona_display_name`

Key observation:
- Both tables have `user_guid`. This is the stable join key if usernames change.

---

### How `user_details` + `user_personas` are populated today (dmsuiusermanager)

DB sync happens **only** when personas are applied/removed via the user-manager app:

- `dmsuiusermanager-nodejs-polarisplatform/server.js`
  - `POST /api/applypersonas`:
    1) Writes tuples to OpenFGA
    2) **Then** calls `UserManagementService.manageuserDetailsAndPersonas(userGuids, personaNames, performedBy)`
- `dmsuiusermanager-nodejs-polarisplatform/src/services/UserManagementService.js`
  - `manageuserDetailsAndPersonas(...)`:
    - Fetches user profile from Keycloak (batch) via `KeycloakService.getUserByUserGuid(userGuids)`
    - **Upserts** into `user_details` (implemented as delete + insert; preserves `last_login_date`)
    - Deletes existing rows in `user_personas` for the `user_guid`
    - Inserts personas + `persona_display_name` for the user
- `dmsuiusermanager-nodejs-polarisplatform/src/services/keycloak.js`
  - `getUserByUserGuid(userGuids)` hits `process.env.KEY_CLOAK_GET_USER_BY_GUID` (POST `{ userIds: [...] }`)
  - Extracts:
    - `userName` from `user.username`
    - `fullName` from `firstName + lastName`
    - `email` from `user.email`
    - **cost center** from `user.attributes.department[0].split(',')[1]`
    - **department** from `user.attributes.department[0].split(',')[2]`
    - `jobTitle` from `user.attributes.job_title[0]`
  - **Does not capture `enabled/disabled` status** today (even though Keycloak user objects usually include `enabled`)

Implications:
- If access was granted in FGA outside this user-manager flow (or before DB-sync existed), the DB can be stale → report wrong/missing.
- If user is disabled in Keycloak later, there is currently no mechanism here to remove them from DB or mark them disabled.
- If username changes in Keycloak, DB will keep stale `user_name` until a re-sync occurs.

---

### Symptom → likely root cause mapping

#### 1) Cost center mismatch (IR cost centers SER400/SER401/INS400/INS401 should become SER402/INS402)
Most likely:
- `user_details.cost_center` still contains legacy codes because:
  - Keycloak attribute still has old codes, **or**
  - Keycloak was updated but DB was not refreshed for all impacted users
- There is no **full re-sync** mechanism that refreshes all users’ profile fields from Keycloak on a schedule / before report generation.

#### 2) Active users missing details (e.g., `ash.allgyer@berkadia.com` has access but missing fields)
Most likely:
- They have access tuples/personas, but `user_details` row is missing or incomplete, and the report starts from `user_details`.
  - Report base table is `user_details`, not `user_personas` or Keycloak.
  - If `user_details` is missing → user will not appear.
  - If Keycloak attributes are missing/format different → `department/cost_center/job_title` can be blank.

#### 3) Disabled users showing up (should be excluded)
Root cause:
- No `enabled/disabled` state is stored in `user_details`
- No filtering step exists in report generator
- No sync mechanism removes/marks disabled users after they are disabled in Keycloak

#### 4) Incorrect username in report (Keycloak correct, report wrong)
Root cause:
- Username is stored in `user_details.user_name` and only refreshed when user-manager runs DB sync
- Report join uses `user_name`, so stale usernames can cause:
  - Wrong username displayed
  - Persona join mismatches if only one table is updated

---

### Recommended approach (use FGA + Keycloak as source of truth; sync DB before reporting)

**Recommendation**: Implement a reliable “pre-report sync” in **`dmsuiusermanager-nodejs-polarisplatform`** (not in the report generator), because user-manager already has:
- OpenFGA access + persona matching (`matchPersonasForUser`)
- Keycloak fetch (`getUserByUserGuid`)
- DB write access to `user_details` / `user_personas`

Design:
1) **Determine the user set**: all user GUIDs that currently have DMS UI access tuples in OpenFGA.
2) **Derive personas** per GUID using `matchPersonasForUser(...)`.
3) **Fetch Keycloak profiles** for those GUIDs in batches (`getUserByUserGuid`), and include:
   - `enabled` (account status) from the Keycloak user representation (not from the ID token)
4) **For enabled users**:
   - Upsert `user_details` (preserve `last_login_date`)
   - Upsert `user_personas` with `persona_display_name`
   - Sync `cost_center` (and other profile fields) from Keycloak so the report reflects Keycloak’s latest state.
     - If Keycloak is already updated to `SER402` / `INS402`, **no explicit mapping is needed**.
     - Optional defense-in-depth: if Keycloak still returns legacy `SER400/SER401/INS400/INS401` for any users, apply a normalization step at sync time.
5) **For disabled users**:
   - Remove from `user_personas` and `user_details` **OR** mark them disabled (requires new column + migration)
6) Update report join to be resilient:
   - Prefer joining `user_details` ↔ `user_personas` on **`user_guid`** (stable), not `user_name`.

Notes:
- This keeps `dmsui-api` report generator simple and makes DB the single source the report uses.
- Users who have never logged in will still appear (because the DB sync creates `user_details` rows), with `last_login_date = NULL`.

---

### Validation / checks (no secrets)

- SQL: find any legacy IR cost centers remaining:
  - `SELECT cost_center, COUNT(*) FROM user_details WHERE cost_center IN ('SER400','SER401','INS400','INS401') GROUP BY cost_center;`
- Confirm example users:
  - `SELECT * FROM user_details WHERE email_id = '<user>';`
  - `SELECT * FROM user_personas WHERE user_guid = '<guid>';`
- After sync, rerun the report endpoint and confirm:
  - Cost center output uses `SER402` / `INS402`
  - Disabled users are absent
  - Username matches Keycloak

---

### Decision log

- **Decision (2026-05-22)**: Use **OpenFGA as the source of truth for “who should be in the report”** (collect GUIDs from tuples), not Keycloak roles.
- **Decision (2026-05-22)**: Use **Keycloak as the source of truth for user profile fields** (`email_id`, `user_name`, `full_name`, `department`, `cost_center`, `job_title`) by implementing a **full resync** into `user_details`.
- **Decision (2026-05-22)**: Do **not** hardcode SER/INS merge mapping as the primary fix; rely on Keycloak returning **SER402/INS402** after resync. Keep legacy→merged normalization only as an optional fallback.
- **Decision (2026-05-22)**: Identify disabled users using Keycloak’s **`enabled`** flag (from user representation); exclude disabled users from the report.
- **Decision (2026-05-22)**: Persist enabled/disabled state in Postgres (e.g. `user_details.is_enabled`) during sync and filter the report on it, instead of calling Keycloak during report generation.
- **Decision (2026-05-22)**: Make the report join resilient by joining tables on **`user_guid`** (stable), not `user_name` (mutable).
- **Decision (2026-05-22)**: Run the full resync as a scheduled job in **`dmsuiusermanager-nodejs-polarisplatform`** and treat `dmsui-api` as read-only for the report.

---

### Scheduling (sync vs report generation)

Current report schedule (K8s):
- `dmsui-api-nodejs-polarisplatform/k8s/qc/cronjob.yaml`: `dmsui-api-user-access-report-processor`
  - `schedule: '0 9 1 * *'` (Asia/Kolkata)

Recommended:
- Add a **user-manager sync cronjob** that runs *before* the report, for buffer/retries.
  - Example: `schedule: '0 8 1 * *'` (Asia/Kolkata)

Triggering options:
- **Preferred**: Cronjob in `dmsuiusermanager-nodejs-polarisplatform` calls a “sync authorized users” endpoint in the same service.
- **Alternative**: Keep cronjob in `dmsui-api-nodejs-polarisplatform` but have it call user-manager sync first, then call `/reports/process-user-access-report/true`.
  - Even in this option, the **sync logic still lives in user-manager** (because it owns FGA + Keycloak admin access).

---

### Verification checklist (to confirm findings are correct)

Use QC data and the example users from the bug description (active-but-missing, disabled-but-showing, incorrect username). The goal is to prove the report is reading stale/incorrect **Postgres** data and not Keycloak.

#### A) Verify the report’s data source (static/code)
- Confirm `dmsui-api-nodejs-polarisplatform` User Access Report reads **only** `user_details` + `user_personas` (no Keycloak calls) and therefore reflects whatever is stored in Postgres at report time.

#### B) Verify with QC data (Keycloak vs Postgres)

For a given user, collect:
- **Keycloak**: `enabled`, `username`, `email`, `firstName/lastName`, and the attribute(s) that contain department/cost center/job title.
- **Postgres**:
  - `SELECT * FROM user_details WHERE email_id = '<email>' OR user_guid = '<guid>';`
  - `SELECT * FROM user_personas WHERE user_guid = '<guid>' OR user_name = '<username>';`

Check these assertions:
- **Cost center mismatch proof**:
  - Keycloak shows `SER402/INS402` (or updated department attribute) but Postgres `user_details.cost_center` still has `SER400/SER401/INS400/INS401`.
- **Disabled user proof**:
  - Keycloak `enabled = false` but the user still exists in Postgres and appears in the report.
- **Incorrect username proof**:
  - Keycloak username differs from `user_details.user_name` (stale in DB) → report shows wrong username.
- **“Missing details” proof** (two common cases):
  - User is in `user_details` but has no matching `user_personas` rows → report “group/persona” columns are blank.
  - User exists in OpenFGA (has DMSUI access tuples) but has no `user_details` row → user absent from report entirely.

Useful diagnostics SQL:
- Users in `user_details` without any personas (by current join key):
  - `SELECT ud.user_guid, ud.user_name, ud.email_id FROM user_details ud LEFT JOIN user_personas up ON ud.user_name = up.user_name WHERE up.id IS NULL;`
- Users where `user_guid` join would work but `user_name` join fails (indicates username drift / inconsistent writes):
  - `SELECT ud.user_guid, ud.user_name, up.user_name AS persona_user_name FROM user_details ud JOIN user_personas up ON ud.user_guid = up.user_guid WHERE ud.user_name <> up.user_name;`

#### C) Verify the Keycloak parsing assumption
`dmsuiusermanager-nodejs-polarisplatform/src/services/keycloak.js` currently parses:
- `costCenter` from `attributes.department[0].split(',')[1]`
- `department` from `attributes.department[0].split(',')[2]`

Validate that QC Keycloak’s attribute format still matches this. If the format changed, DB cost centers can be wrong even after sync.

---

### Manager-ready explanation (copy/paste)

**Current behavior**
- DMS UI access is controlled in **OpenFGA** (tuples/personas).
  - Open: `dmsuiusermanager-nodejs-polarisplatform/server.js` (OpenFGA apply/read flows), `dmsuiusermanager-nodejs-polarisplatform/src/utils/personaMatcher.js` (persona derivation)
- The User Access Report is generated by `dmsui-api` by reading **Postgres tables** `user_details` (user profile) and `user_personas` (personas) and sending an Excel.
  - Open: `dmsui-api-nodejs-polarisplatform/src/services/user-access-report-service.ts`, `dmsui-api-nodejs-polarisplatform/src/routes/reports.ts`, `dmsui-api-nodejs-polarisplatform/src/constants/excel-column-configs.ts`
- Those tables are treated as a **read-model** and are primarily updated by **DMS UI User Manager** when personas are applied (OpenFGA write → DB sync for only those selected users).
  - Open: `dmsuiusermanager-nodejs-polarisplatform/src/services/UserManagementService.js`, `dmsuiusermanager-nodejs-polarisplatform/src/services/keycloak.js`
  - Schema: `dmsuiusermanager-nodejs-polarisplatform/src/db/postgress/migrations/20250115001_create_user_details_table.js`, `dmsuiusermanager-nodejs-polarisplatform/src/db/postgress/migrations/20250115002_create_user_personas_table.js`, `dmsuiusermanager-nodejs-polarisplatform/src/db/postgress/migrations/20251125001_update_user_personas_table.js`
- Report generation is scheduled monthly via a cronjob, but there is no scheduled full refresh of all users into the read-model today.
  - Open: `dmsui-api-nodejs-polarisplatform/k8s/qc/cronjob.yaml` (report schedule), `dmsuiusermanager-nodejs-polarisplatform/server.js` (DB sync only after `/api/applypersonas`)

**Why we see the 3 issues**
1) **Cost center mismatch**
   - Cost center is read from `user_details.cost_center`.
   - If Keycloak cost centers changed (SER402/INS402) but our read-model wasn’t refreshed, the report still shows legacy values.
     - Open: `dmsui-api-nodejs-polarisplatform/src/services/user-access-report-service.ts` (reads `ud.cost_center`), `dmsuiusermanager-nodejs-polarisplatform/src/services/UserManagementService.js` + `dmsuiusermanager-nodejs-polarisplatform/src/services/keycloak.js` (where cost center is fetched/stored)
2) **Active users missing details / users showing without correct fields**
   - The report is driven by what exists in `user_details` + `user_personas`.
   - If a user has access in OpenFGA but was never synced into these tables (or persona join fails), the report will be missing persona/details.
     - Open: `dmsui-api-nodejs-polarisplatform/src/services/user-access-report-service.ts` (base query + `user_name` join), `dmsuiusermanager-nodejs-polarisplatform/server.js` (sync only happens after apply), schema: `dmsuiusermanager-nodejs-polarisplatform/src/db/postgress/migrations/20250115001_create_user_details_table.js`
3) **Disabled users showing & incorrect username**
   - Disabled/enabled is not currently persisted/filtered in the read-model, so disabling in Keycloak doesn’t automatically remove the user from the report.
   - Username in the report is the stored `user_details.user_name`; if it changed in Keycloak but DB wasn’t refreshed, the report shows a stale username.
     - Open: `dmsuiusermanager-nodejs-polarisplatform/src/db/postgress/migrations/20250115001_create_user_details_table.js` (no enabled flag), `dmsuiusermanager-nodejs-polarisplatform/src/services/keycloak.js` (does not map `enabled` today), `dmsui-api-nodejs-polarisplatform/src/services/user-access-report-service.ts` (uses `user_name`)

**What we will do**
- Add a scheduled **pre-report sync** in `dmsuiusermanager` that:
  - enumerates all authorized users from OpenFGA,
  - fetches latest user profile + `enabled` from Keycloak in batches,
  - upserts `user_details`/`user_personas` (preserving `last_login_date`),
  - excludes disabled users,
  - and makes the report join resilient by joining on `user_guid`.
  - Open: `dmsuiusermanager-nodejs-polarisplatform/server.js` (FGA read patterns), `dmsuiusermanager-nodejs-polarisplatform/src/utils/personaMatcher.js`, `dmsuiusermanager-nodejs-polarisplatform/src/services/keycloak.js`, `dmsuiusermanager-nodejs-polarisplatform/src/services/UserManagementService.js`, `dmsui-api-nodejs-polarisplatform/src/services/authTrackingService.ts` (last_login_date behavior)
- Then the report becomes a reliable view of the up-to-date Keycloak-backed read-model.
