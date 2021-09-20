# Scan Types: UDP Scans

`-sU`

## Notes

UDP is stateless and doesn't involve any acknowledgement steps. The system just sends the request and hopes that it reaches. Lack of acknowledgement makes UDP difficult to scan and slower.

When a packet is sent to an open UDP port, there should be no response. Nmap marks it as `open|filtered`. Getting a UDP response is very rare but if received, the port is `open`. When a packet is sent to closed port, the target should respond with `ICMP` (ping) packet containing a message that the port unreachable.

## Questions

1. If a UDP port doesn't respond to an Nmap scan, what will it be marked as?

```
open|filtered
```

2. When a UDP port is closed, by convention the target should send back a "port unreachable" message. Which protocol would it use to do so?

```
ICMP
```
