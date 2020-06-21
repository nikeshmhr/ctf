# Tomghost

## Notes

```
CVE-2020-1938
Exposing flaw in Tomcat AJP protocol
Can be used to read arbitrary file and if webapp has upload functionality then can execute arbitrary code.

export IP=10.10.48.218

Nmap Results:
-------------------------------
PORT     STATE SERVICE    VERSION                                                                        │
22/tcp   open  ssh        OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)                   │
| ssh-hostkey:                                                                                           │
|   2048 f3:c8:9f:0b:6a:c5:fe:95:54:0b:e9:e3:ba:93:db:7c (RSA)                                           │
|   256 dd:1a:09:f5:99:63:a3:43:0d:2d:90:d8:e3:e1:1f:b9 (ECDSA)                                          │
|_  256 48:d1:30:1b:38:6c:c6:53:ea:30:81:80:5d:0c:f1:05 (EdDSA)                                          │
53/tcp   open  tcpwrapped                                                                                │
8009/tcp open  ajp13      Apache Jserv (Protocol v1.3)                                                   │
| ajp-methods:                                                                                           │
|_  Supported methods: GET HEAD POST OPTIONS                                                             │
8080/tcp open  http       Apache Tomcat 9.0.30                                                           │
|_http-favicon: Apache Tomcat                                                                            │
|_http-title: Apache Tomcat/9.0.30                                                                       │
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

## Questions

1. Compromise this machine and obtain user.txt

```
using poc from github https://github.com/nibiwodong/CNVD-2020-10487-Tomcat-ajp-POC

gives us creds skyfuck:8730281lkjlkjdqlksalks

user.txt flag is inside merlin user's directory

THM{GhostCat_1s_so_cr4sy}
```

2. Escalate privileges and obtain root.txt

```
inside skyfuck's home directory we have two files: credential.pgp and tryhackme.asc
copy both files

scp skyfuck@$IP:/home/skyfuck/credential.pgp ./

crack private key
gpg2john
john hash
Result => alexandru

decrypt pgp using cracked password
inside skyfuck's homedir
import secret using => gpg --import tryhackme.asc	(needed, otherwise gives gpg: decryption failed: secret key not available error)
then decrypt file => pgp --decrypt credential.pgp
Result => merlin:asuyusdoiuqoilkda312j31k2j123j1g23g12k3g12kj3gk12jg3k12j3kj123j

ssh as merlin
sudo -l => /usr/bin/zip (seems interesting, lets search for gtfobins)
after becoming root, flag is under /root/ dir

THM{Z1P_1S_FAKE}

```
