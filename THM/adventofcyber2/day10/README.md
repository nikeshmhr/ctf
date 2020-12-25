# Networking: Don't be selfish!

## Notes
```
Learning Objective:
Learn about the basics of network file sharing protocols before getting hands-on with Samba, where you will be enumerating "tbfc-smb-01" : a vulnerable Samba server to gain un-authorised access.

enum4linux tool
```

## Questions
1. Using enum4linux, how many users are there on the Samba server?
```
./enum4linux.pl -U <IP>
3
```

2. Now how many "shares" are there on the Samba server?
```
./enum4linux.pl -S <IP>
4
```

3. Use smbclient to try to login to the shares on the Samba server (10.10.106.87). What share doesn't require a password?
```
from -S flag
tbfc-santa
```

4. Log in to this share, what directory did ElfMcSkidy leave for Santa?
```
jingle-tunes
```