# Scan Types: SYN Scans

`-sS`

## Notes

-   Used to scan port range of a target or targets
-   Also refered as `Half-open` or `Stealth` scan

### Difference from TCP Connect Scans

SYN scan sends back `RST` TCP packets after receiving `SYN/ACK` from the server
![Image](https://i.imgur.com/cPzF0kU.png)

SYN scan and TCP Connect Scan differ in how they handle open port.

## Questions

1. There are two other names for a SYN scan, what are they?

```
half-open stealth
```

2. Can Nmap use a SYN scan without Sudo permissions (Y/N)?

```
N
```
