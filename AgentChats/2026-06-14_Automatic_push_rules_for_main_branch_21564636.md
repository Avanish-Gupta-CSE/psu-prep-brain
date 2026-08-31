# Automatic push rules for main branch

| Metadata | Value |
| :--- | :--- |
| **Chat ID** | `21564636-ab9c-4dd6-955f-f428d51cc1c4` |
| **Created At** | `2026-06-14 15:11:07` |
| **Last Updated At** | `2026-06-14 15:12:00` |
| **Files Touched / Summary** | Edited hooks.json, psu-prep.mdc |
| **Model** | `gemini-3.5-flash` |

---

## 👤 User Message #1

can you read @.brain @.cursor and check if there is any rule regarding automatic push to main
if they remove that rule and make it that I(user) will do it manually

---

## 🤖 Assistant Response

I have read and analyzed your `.brain` and `.cursor` configurations to check for rules regarding automatic git push/sync to the `main` branch.

### What was found
1. **Rule in `.cursor/rules/psu-prep.mdc`**: Under the "Session End Protocol (MANDATORY)" section, there was a rule instructing the AI to commit and push changes to `main` at the end of every conversation to redeploy the mobile portal.
2. **Hook in `.cursor/hooks.json`**: There was a Cursor hook configured for `sessionEnd` that automatically executed the PowerShell script `.cursor/hooks/brain-sync.ps1` to stage, commit, and push changes to the remote repository.

---

### What has been modified
Based on your preference to completely disable the automatic session-end git hook, I have made the following updates:

1. **Updated `.cursor/rules/psu-prep.mdc`**:
   Removed the automatic git sync/push instruction and replaced it with a rule specifying that you will perform git operations manually.

```90:91:.cursor/rules/psu-prep.mdc
4. **Git sync**:
   - The user will commit and push changes manually. Do not perform automatic git sync or push.
```

2. **Updated `.cursor/hooks.json`**:
   Cleared the `sessionEnd` hook from the hooks configuration so that no automatic staging, committing, or pushing occurs when a session ends.

```1:4:.cursor/hooks.json
{
  "version": 1,
  "hooks": {}
}
```

The script `.cursor/hooks/brain-sync.ps1` remains intact in your repository, so you can still run it manually whenever you want to trigger the sync process yourself.

---
