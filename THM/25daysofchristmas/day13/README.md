# Accumulate

```
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-23 19:01 UTC
Nmap scan report for 10.10.137.97
Host is up (0.024s latency).
Not shown: 998 filtered ports
PORT     STATE SERVICE
80/tcp   open  http
3389/tcp open  ms-wbt-server

Nmap done: 1 IP address (1 host up) scanned in 21.49 seconds
```

## Notes

export IP=10.10.137.97

## Questions

1. A web server is running on the target. What is the hidden directory which the website lives on?

```
ffuf -u http://$IP -w dirbuster-2.3-medium
/retro
```

2. Gain initial access and read the contents of user.txt

```
from #1 site author name is revealed as wade.
look into his recent comment and you'll see note parzival
its wordpress site so login with wade:parzival  // DOESNT GIVE ANYTHING FOR THIS QUESTINO
use remmina to connect to server with creds wade:parzival
```

3. [Optional] Elevate privileges and read the content of root.txt

```

```
