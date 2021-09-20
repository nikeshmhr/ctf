# NSE Scripts: Overview

## Notes

Nmap Scripting Engine (NSE) scripts are written in Lua programming language. Scripts are categorized:

-   `safe`:- Won't affect the target
-   `intrusive`:- Not safe: likely to affect the target
-   `vuln`:- Scan for vulnerabilities
-   `exploit`:- Attempt to exploit a vulnerability
-   `auth`:- Attempt to bypass authentication for running services (e.g. Log into an FTP server anonymously)
-   `brute`:- Attempt to bruteforce credentials for running services
-   `discovery`:- Attempt to query running services for further information about the network (e.g. query an SNMP server).

## Questions

1. What language are NSE scripts written in?

```
lua
```

2. Which category of scripts would be a very bad idea to run in a production environment?

```
intrusive
```
