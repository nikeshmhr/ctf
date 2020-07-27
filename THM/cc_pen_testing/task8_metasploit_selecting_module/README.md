# [Section 3 - Metasploit]: - Selecting a module

## Questions

1. How do you select the eternalblue module?

```
use exploit/windows/smb/ms17_010_eternalblue
```

2. What option allows you to select the target host(s)?

```
RHOSTS
```

3. How do you set the target port?

```
RPORT
```

4. What command allows you to set options?

```
set
```

5. How would you set SMBPass to "username"?

```
set SMBPass username
```

6. How would you set the SMBUser to "password"?

```
set SMBUser password
```

7. What option sets the architecture to be exploited?

```
arch
```

8. What option sets the payload to be sent to the target machine?

```
payload
```

9. Once you've finished setting all the required options, how do you run the exploit?

```
exploit
```

10. What flag do you set if you want the exploit to run in the background?

```
-j
```

11. How do you list all current sessions?

```
sessions
```

12. What flag allows you to go into interactive mode with a session("drops you either into a meterpreter or regular shell")

```
-i
```
