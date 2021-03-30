# Wgel CTF

## Notes
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 94:96:1b:66:80:1b:76:48:68:2d:14:b5:9a:01:aa:aa (RSA)
|   256 18:f7:10:cc:5f:40:f6:cf:92:f8:69:16:e2:48:f4:38 (ECDSA)
|_  256 b9:0b:97:2e:45:9b:f3:2a:4b:11:c7:83:10:33:e0:ce (EdDSA)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

<!-- Jessie don't forget to udate the webiste -->

http://10.10.62.44/sitemap/

unapp template
https://www.exploit-db.com/exploits/21742
https://github.com/ColorlibHQ/unapp

dirsearch /sitemap with common wordlist
.ssh/id_rsa (private keys)

ssh2john says
id_rsa has no password!

ssh with jessie
chmod 600 id_rsa
ssh -i id_rsa jessie@ip

sudo -l

wget is executable as root without password

gtfobin
https://vk9-sec.com/wget-privilege-escalation/

educated guessing root flag location and name `/root/root_flag.txt`

## Question
1. User flag
```
explore Documents folder
057c67131c3d5e42dd5cd3075b198ff6
```

2. Root flag
```
b1b968b37519ad1daa6408188649263d
```