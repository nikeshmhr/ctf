# Startup - Welcome to Spice Hut!

Abuse traditional vulnerabilities via untraditional means.

We ask that you perform a thorough penetration test and try to own root

## Notes
`nmap -sv -sV IP`
```
PORT     STATE    SERVICE      VERSION
21/tcp   open     ftp          vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| drwxrwxrwx    2 65534    65534        4096 Nov 12 04:53 ftp [NSE: writeable]
| -rw-r--r--    1 0        0          251631 Nov 12 04:02 important.jpg
|_-rw-r--r--    1 0        0             208 Nov 12 04:53 notice.txt
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to 10.9.18.129
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp   open     ssh          OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 b9:a6:0b:84:1d:22:01:a4:01:30:48:43:61:2b:ab:94 (RSA)
|   256 ec:13:25:8c:18:20:36:e6:ce:91:0e:16:26:eb:a2:be (ECDSA)
|_  256 a2:ff:2a:72:81:aa:a2:9f:55:a4:dc:92:23:e6:b4:3f (EdDSA)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Maintenance
3995/tcp filtered iss-mgmt-ssl
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

```
* ftp connect and can upload inside ftp/ directory
* dirsearch shows /files which shows contents of ftp
* php is executable inside files/ftp directory
* upload revershell
* to stablize shell
    * python -c "import pty;pty.spawn('/bin/bash')"

-----------------------------------------

* incidents is suspicious directory
* analyze pcap
* c4ntg3t3n0ughsp1c3 being used for lennie
* su lennie with above password (stablizing shell is important inorder to run su) - https://blog.ropnop.com/upgrading-simple-shells-to-fully-interactive-ttys/

------------------------------------------

* scripts/planner.sh is run as root
* which runs lennie defined script /etc/print.sh
* get another shell by overriding /etc/print.sh or just cat out file content to some readable directory

----------------------------------------------------------

## Questions
1. What is the secret spicy soup recipe?
```
recipe.txt

love
```

2. What are the contents of user.txt?
```
THM{03ce3d619b80ccbfb3b7fc81e46c0e79}
```

3. What are the contents of root.txt?
```
THM{f963aaa6a430f210222158ae15c3d76d}
```