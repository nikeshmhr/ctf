# [Section 6 - Samba]: smbmap


## Notes
https://github.com/ShawnDEvans/smbmap

## Questions
1. How do you set the username to authenticate with?
```
-u
```

2. What about the password?
```
-p
```

3. How do you set the host?
```
-h
```

4. What flag runs a command on the server(assuming you have permissions that is)?
```
-x
```

5. How do you specify the share to enumerate?
```
-s
```

6. How do you set which domain to enumerate?
```
-d
```

7. What flag downloads a file?
```
--download
```

8. What about uploading one?
```
--upload
```

9. Given the username "admin", the password "password", and the ip "10.10.10.10", how would you run ipconfig on that machine
```
smbmap -u "admin" -p "password" -h "10.10.10.10" -x "ipconfig"
```