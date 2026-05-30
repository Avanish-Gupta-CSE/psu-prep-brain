# CN — OSI Model (7 Layers)

> 🎯 Target: Name all 7 layers top-to-bottom + their KEY function + one protocol each in 40s.
> ⏱️ Read time: 12 minutes
> ★ HIGH PRIORITY — OSI is the #1 most asked CN topic in PSU interviews.

---

## What Is OSI Model?

**Open Systems Interconnection** — a conceptual framework that standardizes how different network systems communicate with each other in **7 layers**.

> Think of it as a **postal system** — your letter (data) goes through multiple departments (layers), each adding/removing its own label (header/trailer), before reaching the destination.

---

## The Mnemonic — Never Forget This

### Top to Bottom (Layer 7 → 1):
> **"All People Seem To Need Data Processing"**
> **A**pplication → **P**resentation → **S**ession → **T**ransport → **N**etwork → **D**ata Link → **P**hysical

### Bottom to Top (Layer 1 → 7):
> **"Please Do Not Throw Sausage Pizza Away"**
> **P**hysical → **D**ata Link → **N**etwork → **T**ransport → **S**ession → **P**resentation → **A**pplication

### Hinglish Version (Bottom to Top):
> **"Pehle Data Nikalte Hain, Transport Se Prapt Aata"**
> **P**hysical, **D**ata Link, **N**etwork, **T**ransport, **S**ession, **P**resentation, **A**pplication

---

## Data Unit Names Per Layer

```
Application  }
Presentation } → Data
Session      }
Transport      → Segment
Network        → Packet
Data Link      → Frame
Physical       → Bits
```

> **Mnemonic:** "**Data Sent Neatly, Packets Find Bits**" (top to bottom)

---

## All 7 Layers — Full Detail

### Layer 7 — Application Layer
> **"Tumhara interface hai duniya se"** — where YOU interact with the network

| | Details |
|---|---|
| **Function** | Network virtual terminal, Mail services, Directory services |
| **What it does** | Provides services to user applications; window to access network |
| **Examples** | Browsers, Skype, Messenger |
| **Protocols** | **SMTP** (email), **HTTP/HTTPS** (web), **FTP** (file), **POP3** (email receive), **SNMP**, **Telnet** |
| **Devices** | — (end-user software layer) |

---

### Layer 6 — Presentation Layer
> **"Translator hai"** — converts data to a format the other side understands

| | Details |
|---|---|
| **Also called** | Translation Layer |
| **Function** | Translation (ASCII ↔ EBCDIC), Encryption/Decryption, Compression |
| **What it does** | Ensures data is in the right format for transmission and display |
| **Protocols** | **MPEG** (video), **SSL/TLS** (encryption), **MIME** (email format), **XDR** |
| **Devices** | — |

> **Key 3 jobs:** Translate + Encrypt + Compress

---

### Layer 5 — Session Layer
> **"Meeting arrange karta hai"** — manages the conversation

| | Details |
|---|---|
| **Function** | Session establishment, maintenance, termination; Synchronization; Dialog control |
| **What it does** | Sets up, manages, and tears down sessions between applications |
| **Protocols** | **NetBIOS**, **SAP**, **PPTP**, **ADSP**, **PAP** |
| **Devices** | Gateway, Servers |

> **Key 3 jobs:** Establish + Maintain + Terminate session

---

### Layer 4 — Transport Layer
> **"Delivery guarantee karta hai"** — end-to-end reliable delivery

| | Details |
|---|---|
| **Data unit** | **Segment** |
| **Function** | Segmentation & reassembly; End-to-end delivery; Service point addressing; Acknowledgement; Retransmission on error |
| **What it does** | Breaks large messages into segments, ensures complete delivery, reassembles at destination |
| **Protocols** | **TCP** (reliable), **UDP** (fast, unreliable), **SPX** |
| **Devices** | Firewall, Gateway |

> **TCP vs UDP:**
> - TCP = reliable, connection-oriented, slower (handshake)
> - UDP = unreliable, connectionless, faster (no handshake)

---

### Layer 3 — Network Layer
> **"GPS hai"** — finds the best path and handles IP addresses

| | Details |
|---|---|
| **Data unit** | **Packet** |
| **Function** | Routing; Logical Addressing (IP); Subnet traffic control |
| **What it does** | Places sender/receiver IP addresses in packet header; determines best route |
| **Protocols** | **IPv4**, **IPv6**, **ICMP** (ping), **IPSEC**, **MPLS** |
| **Devices** | **Router**, Brouter |

> **Key point:** Network layer adds **IP addresses** (logical addressing). Data Link layer adds **MAC addresses** (physical addressing).

---

### Layer 2 — Data Link Layer
> **"Dono paas ke stations ke beech" (node-to-node)** — local delivery, error-free

| | Details |
|---|---|
| **Data unit** | **Frame** |
| **Function** | Framing; Physical addressing (MAC); Error control; Flow control; Access control |
| **What it does** | Packages bits into frames; ensures error-free transfer between adjacent nodes |
| **Protocols** | **PPP**, **ARP** (IP→MAC), **Frame Relay**, **ATM**, Fiber Cable |
| **Devices** | **Switch**, **Bridge**, Access Point |

> **ARP** = Address Resolution Protocol — converts IP address to MAC address

---

### Layer 1 — Physical Layer
> **"Wires aur bits"** — actual physical transmission of raw bits

| | Details |
|---|---|
| **Data unit** | **Bits (0s and 1s)** |
| **Function** | Bit synchronization; Bit rate control; Physical topologies; Transmission mode |
| **What it does** | Converts signals to 0s and 1s; sends bits over the physical medium |
| **Protocols** | **RJ-45**, **100 Base Tx**, **ISDN** |
| **Devices** | **Hub**, NIC (Network Interface Card), Cable, Modem, Wireless Repeaters |

---

## All 7 Layers — Master Table

| Layer | Name | Data Unit | Key Function | Protocols | Device |
|---|---|---|---|---|---|
| 7 | Application | Data | User interface to network | HTTP, FTP, SMTP, Telnet | — |
| 6 | Presentation | Data | Translate, Encrypt, Compress | SSL, MPEG, MIME | — |
| 5 | Session | Data | Establish/maintain/terminate sessions | NetBIOS, PPTP | Gateway |
| 4 | Transport | **Segment** | End-to-end delivery, segmentation | **TCP, UDP** | Firewall |
| 3 | Network | **Packet** | Routing + IP addressing | **IPv4, IPv6, ICMP** | **Router** |
| 2 | Data Link | **Frame** | Node-to-node, MAC, error control | ARP, PPP | **Switch** |
| 1 | Physical | **Bits** | Raw bit transmission | RJ-45, ISDN | **Hub** |

---

## OSI vs TCP/IP Model — Quick Comparison

| OSI (7 layers) | TCP/IP (4 layers) |
|---|---|
| Application (7) | Application |
| Presentation (6) | Application |
| Session (5) | Application |
| Transport (4) | Transport |
| Network (3) | Internet |
| Data Link (2) | Network Access |
| Physical (1) | Network Access |

> TCP/IP **merges** Application+Presentation+Session into one Application layer, and merges Data Link+Physical into Network Access.

---

## Quick Cheat — Layer Responsibilities in One Word

```
Layer 7 Application  → USER
Layer 6 Presentation → TRANSLATE
Layer 5 Session      → MANAGE
Layer 4 Transport    → DELIVER (TCP/UDP)
Layer 3 Network      → ROUTE   (IP + Router)
Layer 2 Data Link    → FRAME   (MAC + Switch)
Layer 1 Physical     → BITS    (Hub + Wire)
```

---

## Your 40-Second Script — OSI Model

> *"OSI model has 7 layers. Bottom to top: Physical transmits raw bits, Data Link handles
> node-to-node delivery using MAC addresses and frames, Network handles routing and IP
> addressing using packets, Transport ensures end-to-end delivery using TCP or UDP in
> segments, Session manages connections, Presentation handles translation and encryption,
> Application is the user-facing layer with protocols like HTTP and FTP.
> Mnemonic bottom-up: Please Do Not Throw Sausage Pizza Away."*

---

## Follow-Up Questions

**Q: What is the difference between TCP and UDP?**
> TCP is connection-oriented, reliable, provides acknowledgement and retransmission — used for HTTP, email, file transfer. UDP is connectionless, faster, no guarantee of delivery — used for video streaming, DNS, gaming where speed > reliability.

**Q: What is the difference between Switch and Router?**
> Switch operates at Layer 2 (Data Link) — uses MAC addresses, connects devices within the same network. Router operates at Layer 3 (Network) — uses IP addresses, connects different networks.

**Q: What is ARP?**
> Address Resolution Protocol (Layer 2) — resolves an IP address to its corresponding MAC address. When a device knows the IP but needs the MAC to send a frame on the local network, it broadcasts an ARP request.

**Q: Which layer adds IP address? Which adds MAC address?**
> Network Layer (3) adds IP address (logical). Data Link Layer (2) adds MAC address (physical).
