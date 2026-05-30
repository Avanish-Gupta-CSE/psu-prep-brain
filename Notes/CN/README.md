# CN — Computer Networks Study Notes Index

> Format: Definition + Mnemonic (Hinglish) + Example + 40s script + Follow-ups.

---

## Revision Order

```
Step 1 → 01-DATA-COMM-AND-BASICS.md   5 components + 3 data flow modes (10 min)
Step 2 → 02-OSI-MODEL.md              7 layers — HIGH PRIORITY (15 min)
Step 3 → 03-NETWORK-TOPOLOGY.md       6 topologies + comparison table (12 min)
```

> **Day-before quick revision:** Cheat sheet at bottom of each file only.
> **OSI model is #1 priority** — say the mnemonic aloud 3 times right now.

---

## Files

| File | Topics | Read Time | Status |
|---|---|---|---|
| `01-DATA-COMM-AND-BASICS.md` | 5 DC components, Simplex/Half/Full Duplex, Network criteria, Point-to-point vs Multipoint | 8 min | ✅ Done |
| `02-OSI-MODEL.md` | All 7 layers (function, protocol, device, data unit), OSI vs TCP/IP | 12 min | ✅ Done |
| `03-NETWORK-TOPOLOGY.md` | 6 topologies with full comparison (advantage, disadvantage, reliability, cost, links formula) | 12 min | ✅ Done |

---

## Master Cheat Sheet

```
Data Communication:
  5 components → MSRTP → "Mere Saath Raho Tum Pyaar se"
  Message, Sender, Receiver, Transmission Medium, Protocol

Data Flow:
  Simplex   → Sirf ek taraf    (radio, keyboard)
  Half Duplex → Baari baari    (walkie-talkie)
  Full Duplex → Ek saath dono  (phone call)

OSI 7 Layers (Bottom → Top):
  "Please Do Not Throw Sausage Pizza Away"
  Physical → Data Link → Network → Transport → Session → Presentation → Application

Data Units:
  Physical=Bits, Data Link=Frame, Network=Packet, Transport=Segment, Upper 3=Data

Key Layer Facts:
  Layer 1 Physical   → Hub, raw bits, RJ-45
  Layer 2 Data Link  → Switch, Frame, MAC address, ARP
  Layer 3 Network    → Router, Packet, IP address, ICMP
  Layer 4 Transport  → Firewall, Segment, TCP/UDP
  Layer 7 Application → HTTP, FTP, SMTP, Telnet

TCP vs UDP:
  TCP → reliable, connection-oriented, slower (email, web, file)
  UDP → unreliable, connectionless, faster (video, DNS, gaming)

Topologies (6): "Bahut Star Ring Tree Mesh Hybrid hai"
  Bus    → single cable, cheap, backbone fail = all down
  Star   → central hub, easy, hub fail = all down, max 100m
  Ring   → unidirectional, one node fail = all down
  Tree   → hierarchical star, root fail = all down
  Mesh   → n(n-1)/2 links, most reliable, most expensive
  Hybrid → combination, most complex, worst security

Topology quick pick:
  Most reliable  → Mesh
  Most common office → Star
  Most scalable  → Tree
  Most complex   → Hybrid
```

---

## Topics To Add (Next Pages)

- [ ] TCP/IP protocol stack detail
- [ ] IP addressing — IPv4, subnetting, CIDR
- [ ] DNS — resolution process (step-by-step)
- [ ] HTTP vs HTTPS
- [ ] Error detection/correction (CRC, parity)
- [ ] Routing protocols (RIP, OSPF, BGP)
