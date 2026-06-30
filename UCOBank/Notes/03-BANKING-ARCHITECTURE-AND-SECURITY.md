# 03. Banking Technology, Architecture & Security

Modern banking is entirely digital. This note covers the technological infrastructure of a commercial bank and the cybersecurity frameworks required to protect financial transactions.

---

## 1. Core Banking Solution (CBS) & Finacle

The Core Banking Solution (CBS) is the central nervous system of a bank. It integrates all branches, customer accounts, and transaction channels into a single, real-time database.

### Finacle Architecture
UCO Bank uses **Finacle** (developed by EdgeVerve/Infosys), which is the industry standard for Indian public sector banks.

```
┌────────────────────────────────────────────────────────────────────────┐
│                        DIGITAL CHANNELS LAYER                          │
│   (UCO mBanking Plus, Internet Banking, ATMs, UPI, Third-Party APIs)   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ (Secure REST APIs / HTTPS)
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                           API GATEWAY LAYER                            │
│           (Rate Limiting, Authentication, WAF, SSL Termination)        │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ (ISO 8583 / ISO 20022 Protocols)
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                        FINACLE CORE ENGINE                             │
│       (General Ledger, Customer Master (CIF), Transaction Engine)      │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                     CENTRAL TRANSACTION DATABASE                       │
│              (Highly Normalized Oracle/PostgreSQL RDBMS)               │
└────────────────────────────────────────────────────────────────────────┘
```

### Key Components of CBS:
1.  **Customer Information File (CIF)**: A unique identifier (CIF Number) that aggregates all accounts (Savings, Current, FD, Loans) belonging to a single customer, enabling a 360-degree customer view.
2.  **General Ledger (GL)**: The master accounting record of the bank. Every transaction must balance (Double-Entry Bookkeeping) and update the GL in real-time.
3.  **Transaction Processing Engine**: Processes debits, credits, interest calculations, and fee charges, ensuring ACID compliance.

### Your Role as a Developer:
You will not be modifying Finacle's core COBOL or proprietary code. Instead, you will build **secure, high-performance middleware and REST APIs** at the **API Gateway Layer** to connect modern digital frontends (like mobile apps) to the core banking engine.

---

## 2. Payment & Settlement Systems in India

Understanding how money moves between accounts and across different banks is a core requirement for a banking IT Officer.

### 1. NEFT (National Electronic Funds Transfer)
*   **Operator**: Reserve Bank of India (RBI).
*   **Mechanism**: **Deferred Net Settlement (DNS)**. Transactions are not processed instantly; they are grouped and settled in half-hourly batches.
*   **Limits**: No minimum or maximum limit.
*   **Availability**: 24x7x365.

### 2. RTGS (Real Time Gross Settlement)
*   **Operator**: Reserve Bank of India (RBI).
*   **Mechanism**: **Real-Time Gross Settlement**. Transactions are settled continuously and individually on a transaction-by-transaction basis.
*   **Limits**: **Minimum limit is ₹2 Lakhs**. No maximum limit. Used for high-value corporate and inter-bank settlements.
*   **Availability**: 24x7x365.

### 3. IMPS (Immediate Payment Service)
*   **Operator**: National Payments Corporation of India (NPCI).
*   **Mechanism**: Instant, real-time inter-bank electronic fund transfer.
*   **Limits**: Maximum limit is ₹5 Lakhs.
*   **Availability**: 24x7x365.

### 4. UPI (Unified Payments Interface)
*   **Operator**: National Payments Corporation of India (NPCI).
*   **Mechanism**: Built on top of the IMPS infrastructure. It allows instant mobile-to-mobile payments using a **Virtual Payment Address (VPA)** (e.g., `avanish@uco`) without sharing sensitive bank account numbers or IFSC codes. It uses single-click 2-factor authentication (your mobile device + UPI PIN).

### 5. UPI Lite (On-Device Wallet)
*   **The Problem**: Over 50% of UPI transactions in India are micro-transactions under ₹200. Processing millions of small transactions was putting a massive query load on banks' core CBS databases, causing transactional latency and server crashes.
*   **The Solution**: UPI Lite is an on-device wallet. You pre-load up to ₹2,000 into the wallet. Transactions up to ₹500 are processed directly on your device's local storage without hitting the bank's core CBS database in real-time. The wallet balance is synced with the bank periodically in batches, reducing CBS database load by up to 40%.

### 6. CBDC (Central Bank Digital Currency / e-Rupee)
*   **What is it?** It is a digital token issued by the RBI that represents sovereign currency (legal tender).
*   **Difference between UPI and CBDC**:
    *   *UPI*: UPI is a payment mechanism. When you pay via UPI, commercial bank deposits move from Account A to Account B. It requires inter-bank settlement.
    *   *CBDC*: CBDC is the money itself. It is digital legal tender. When you pay via CBDC, the digital cash moves directly from your digital wallet to the receiver's digital wallet, mimicking physical cash. There is no commercial bank intermediary or settlement delay.

---

## 3. Cybersecurity in Banking

In banking, security is not a feature; it is a non-negotiable prerequisite.

### 1. Zero Trust Architecture
*   **Core Principle**: "Never trust, always verify."
*   **Mechanism**: Traditional security relied on a "perimeter" (firewalls protecting the internal network). Zero Trust assumes that threats exist both inside and outside the network. Every user, device, and API call must be authenticated, authorized, and encrypted, regardless of where the request originates.
*   **Your Experience**: *"At Berkadia, we implemented Zero Trust by integrating **Keycloak SSO** for identity propagation and **OpenFGA** (Fine-Grained Authorization) to enforce strict, role-based access control down to individual document classes. This prevents unauthorized internal or external access."*

### 2. DDoS (Distributed Denial of Service) Defense
*   **The Threat**: Attackers flood banking servers with millions of fake requests, crashing the mobile banking app and website.
*   **Defense Strategy**:
    *   **Rate Limiting**: Restricting the number of requests an IP address can make per minute.
    *   **Web Application Firewall (WAF)**: Filtering out malicious traffic patterns.
    *   **Traffic Scrubbing**: Routing traffic through scrubbing centers (like Cloudflare or AWS Shield) that separate legitimate customer traffic from botnet traffic.

### 3. SSL/TLS Handshake (Securing Data in Transit)
Every transaction between a mobile app and the bank's servers must be encrypted using SSL/TLS.
*   **The Steps**:
    1.  *Client Hello*: Client sends supported TLS versions and cipher suites.
    2.  *Server Hello*: Server responds with selected TLS version, cipher suite, and its **Digital Certificate** (containing the public key).
    3.  *Authentication*: Client verifies the server's certificate with a trusted Certificate Authority (CA).
    4.  *Key Exchange*: Client generates a pre-master secret, encrypts it with the server's public key, and sends it to the server.
    5.  *Session Key*: Both parties generate a symmetric **Session Key** from the pre-master secret. All subsequent communication is encrypted using this session key (symmetric encryption is much faster than asymmetric encryption).

### 4. OWASP Top 10 & Secure Coding
You must write code that is secure by design.

#### SQL Injection (SQLi)
*   **The Threat**: Attackers inject malicious SQL code into input fields to manipulate the database.
    *   *Vulnerable Code*: `String query = "SELECT * FROM users WHERE user = '" + inputUser + "' AND pass = '" + inputPass + "'";`
*   **The Defense**: Always use **Parameterized Queries (Prepared Statements)**. This treats user input strictly as data, not executable code.
    *   *Secure Code*:
        ```java
        PreparedStatement pstmt = connection.prepareStatement("SELECT * FROM users WHERE user = ? AND pass = ?");
        pstmt.setString(1, inputUser);
        pstmt.setString(2, inputPass);
        ```

#### Cross-Site Scripting (XSS)
*   **The Threat**: Attackers inject malicious scripts into web pages viewed by other users.
*   **The Defense**: Sanitize and escape all user inputs before rendering them in the browser. Use Content Security Policies (CSP).

#### Broken Object Level Authorization (BOLA)
*   **The Threat**: A user accesses another user's account by modifying the ID in the API request (e.g., changing `/api/accounts/101` to `/api/accounts/102`).
*   **The Defense**: Never trust the client-side ID. Always validate that the authenticated user session (from the JWT/SSO token) has explicit permissions to access the requested resource ID.
