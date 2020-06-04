# Reconnaissance

## Notes

```
nmap -sV -Pn -A 10.10.17.38

Starting Nmap 7.60 ( https://nmap.org ) at 2020-06-04 18:24 +0545                                        │
Nmap scan report for 10.10.17.38                                                                         │
Host is up (0.29s latency).                                                                              │
Not shown: 994 closed ports                                                                              │
PORT     STATE SERVICE     VERSION                                                                       │
21/tcp   open  ftp         vsftpd 3.0.3                                                                  │
22/tcp   open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)                  │
| ssh-hostkey:                                                                                           │
|   2048 5a:4f:fc:b8:c8:76:1c:b5:85:1c:ac:b2:86:41:1c:5a (RSA)                                           │
|   256 ac:9d:ec:44:61:0c:28:85:00:88:e9:68:e9:d0:cb:3d (ECDSA)                                          │
|_  256 30:50:cb:70:5a:86:57:22:cb:52:d9:36:34:dc:a5:58 (EdDSA)                                          │
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)                                   │
445/tcp  open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)                               │
3128/tcp open  http-proxy  Squid http proxy 3.5.12                                                       │
|_http-server-header: squid/3.5.12                                                                       │
|_http-title: ERROR: The requested URL could not be retrieved                                            │
3333/tcp open  http        Apache httpd 2.4.18 ((Ubuntu))                                                │
|_http-server-header: Apache/2.4.18 (Ubuntu)                                                             │
|_http-title: Vuln University                                                                            │
Service Info: Host: VULNUNIVERSITY; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel                     │
                                                                                                         │
Host script results:                                                                                     │
|_nbstat: NetBIOS name: VULNUNIVERSITY, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)        │
| smb-os-discovery:                                                                                      │
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)                                                                │
|   Computer name: vulnuniversity                                                                        │
|   NetBIOS computer name: VULNUNIVERSITY\x00                                                            │
|   Domain name: \x00                                                                                    │
|   FQDN: vulnuniversity                                                                                 │
|_  System time: 2020-06-04T08:40:45-04:00                                                               │
| smb-security-mode:                                                                                     │
|   account_used: guest                                                                                  │
|   authentication_level: user                                                                           │
|   challenge_response: supported                                                                        │
|_  message_signing: disabled (dangerous, but default)                                                   │
| smb2-security-mode:                                                                                    │
|   2.02:                                                                                                │
|_    Message signing enabled but not required                                                           │
| smb2-time:                                                                                             │
|   date: 2020-06-04 18:25:45                                                                            │
|_  start_date: 1601-01-01 05:41:16                                                                      │
                                                                                                         │
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .           │
Nmap done: 1 IP address (1 host up) scanned in 77.43 seconds
```

## Questions

2. Scan the box, how many ports are open?

```
6
```

3. What version of the squid proxy is running on the machine?

```
3.5.12
```

4. How many ports will nmap scan if the flag -p-400 was used?

```
1 to 400

400
```

5. Using the nmap flag -n what will it not resolve?

```
dns

```

6. What is the most likely operating system this machine is running?

```
ubuntu
```

7. What port is the web server running on?

```
3333
```
