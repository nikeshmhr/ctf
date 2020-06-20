# Host Enumeration

## Notes

```
nmap -sC -sV => useful for basic analysis on service running, version info
PORT      STATE    SERVICE                                                                               │
22/tcp    open     ssh        OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:                                                                                           │
|   2048 6d:2c:40:1b:6c:15:7c:fc:bf:9b:55:22:61:2a:56:fc (RSA)                                           │
|   256 ff:89:32:98:f4:77:9c:09:39:f5:af:4a:4f:08:d6:f5 (ECDSA)                                          │
|_  256 89:92:63:e7:1d:2b:3a:af:6c:f9:39:56:5b:55:7e:f9 (EdDSA)                                          │
80/tcp    open     http     Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works                                                      │
1034/tcp  filtered zincite-a                                                                             │
1074/tcp  filtered warmspotMgmt                                                                          │
3871/tcp  filtered avocent-adsap                                                                         │
9876/tcp  filtered sd                                                                                    │
27352/tcp filtered unknown


```

## Questions

1. How many ports are open on the target machine?

```
2
```

2. What is the http-title of the web server?

```
Apache2 Ubuntu Default Page: It works
```

3. What version is the ssh service?

```
OpenSSH 7.2p2 Ubuntu 4ubuntu2.8
```

4. What is the version of the web server?

```
Apache/2.4.18
```
