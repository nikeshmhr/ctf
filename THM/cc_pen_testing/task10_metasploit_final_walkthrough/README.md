#  [Section 3 - Metasploit]: Final Walkthrough

## Notes
```
```

## Question
1. Select the module that needs to be exploited
```
use exploit/multi/http/nostromo_code_execs
```

2. What variable do you need to set, to select the remote host
```
rhosts
```

3. How do you set the port to 80
```
set rport 80
```

4. How do you set listening address(Your machine)
```
lhost
```

5. What is the name of the secret directory in the /var/nostromo/htdocs directory?
```
s3cretd1r
```

6. What are the contents of the file inside of the directory?
```
Woohoo!
```