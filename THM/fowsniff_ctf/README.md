# Hack into the FowSniff organization

## Notes
Starting Nmap 7.60 ( https://nmap.org ) at 2021-02-24 20:35 +0545
Nmap scan report for 10.10.119.114
Host is up (0.25s latency).
Not shown: 995 closed ports
PORT    STATE    SERVICE     VERSION
22/tcp  open     ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 90:35:66:f4:c6:d2:95:12:1b:e8:cd:de:aa:4e:03:23 (RSA)
|   256 53:9d:23:67:34:cf:0a:d5:5a:9a:11:74:bd:fd:de:71 (ECDSA)
|_  256 a2:8f:db:ae:9e:3d:c9:e6:a9:ca:03:b1:d7:1b:66:83 (EdDSA)
80/tcp  open     http        Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Fowsniff Corp - Delivering Solutions
110/tcp open     pop3        Dovecot pop3d
|_pop3-capabilities: RESP-CODES UIDL USER SASL(PLAIN) PIPELINING TOP CAPA AUTH-RESP-CODE
143/tcp open     imap        Dovecot imapd
911/tcp filtered xact-backup
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

pastebin https://pastebin.com/NrAqVeeX

mauer@fowsniff:8a28a94a588a95b80163709ab4313aa4         mailcall
mustikka@fowsniff:ae1644dac5b77c0cf51e0d26ad6d7e56      bilbo101
tegel@fowsniff:1dc352435fecca338acfd4be10984009         apples01
baksteen@fowsniff:19f5af754c31f1e2651edde9250d69bb      skyler22
seina@fowsniff:90dc16d47114aa13671c697fd506cf26         scoobydoo2
stone@fowsniff:a92b8a29ef1183192e3d35187e0cfabd
mursten@fowsniff:0e9588cb62f4b6f27e33d449e2ba0b3b       carp4ever    
parede@fowsniff:4d6e42f56e127803285a0a7649b5ab11        orlando12    
sciana@fowsniff:f7fd98d380735e859f8b2ffbbede5a7e        07011972

nc ip 110

user `<username>`
pass `<password>`
list
retr `no.`

## Questions
1. What was seina's password to the email service?
```
scoobydoo2
```

2. Looking through her emails, what was a temporary password set for her?
```
S1ck3nBluff+secureshell
```