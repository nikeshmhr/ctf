# [Section 6 - Samba]: smbclient


## Notes
https://www.samba.org/samba/docs/current/man-html/smbclient.1.html

Impacket => https://github.com/SecureAuthCorp/impacket

## Questions
1. How do you specify which domain(workgroup) to use when connecting to the host?
```
-w
```

2. How do you specify the ip address of the host?
```
-i
```

3. How do you run the command "ipconfig" on the target machine?
```
-c "ipconfig"
```

4. How do you specify the username to authenticate with?
```
-u
```

5. How do you specify the password to authenticate with?
```
-p
```

6. What flag is set to tell smbclient to not use a password?
```
-n
```

7. While in the interactive prompt, how would you download the file test, assuming it was in the current directory?
```
get test
```

8. In the interactive prompt, how would you upload your /etc/hosts file
```
put /etc/hosts
```