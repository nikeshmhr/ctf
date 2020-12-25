# Special by DarkStar The Trial Before Christmas

## Notes
```
10.10.187.58

python3 -c 'import pty;pty.spawn("/bin/bash")'
export TERM=xterm
stty raw -echo; fg
```

## Questions
1. Scan the machine. What ports are open?
```
80, 65000
```

2. What's the title of the hidden website? It's worthwhile looking recursively at all websites on the box for this step. 
```
Light Cycle
```

3. What is the name of the hidden php page?
```
uploads.php
```

4. What is the name of the hidden directory where file uploads are saved?
```
grid
```

5. What is the value of the web.txt flag?
```
THM{ENTER_THE_GRID}
```

6. Review the configuration files for the webserver to find some useful loot in the form of credentials. What credentials do you find? username:password
```
tron:IFightForTheUsers
```

7. Access the database and discover the encrypted credentials. What is the name of the database you find these in?
```
tron
```

8. Crack the password. What is it?
```
+----+----------+----------------------------------+
| id | username | password                         |
+----+----------+----------------------------------+
|  1 | flynn    | edc621628f6d19a13a00fd683f5e3ff7 |
+----+----------+----------------------------------+
@computer@
```

9. What is the value of the user.txt flag?
```
THM{IDENTITY_DISC_RECOGNISED}
```

10. Check the user's groups. Which group can be leveraged to escalate privileges? 
```
lxd
```

11. What is the value of the root.txt flag?
```
THM{FLYNN_LIVES}
```