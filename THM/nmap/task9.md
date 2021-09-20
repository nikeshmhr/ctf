# Scan Types: ICMP Network Scanning

## Notes

-   Ping sweep to each possible IP
-   We use `-sn`
-   `nmap -sn 192.168.1.1-254`
-   `nmap -sn 192.168.0.0/24`

## Question

1. How would you perform a ping sweep on the 172.16.x.x network (Netmask: 255.255.0.0) using Nmap? (CIDR notation)

```
nmap -sn 172.16.0.0/16
```
