# Find flags!

## Notes

## Questions
1. Flag1? This flag can be found at the system root. 
```
C:/flag1.txt
flag{access_the_machine}
```

2. Flag2? This flag can be found at the location where passwords are stored within Windows.
*Errata: Windows really doesn't like the location of this flag and can occasionally delete it. It may be necessary in some cases to terminate/restart the machine and rerun the exploit to find this flag. This relatively rare, however, it can happen. 
```
google > windows password storage location
C:\windows\system32\config\SAM

cat C:\windows\system32\config\flag2.txt

flag{sam_database_elevated_access}
```

3. flag3? This flag can be found in an excellent location to loot. After all, Administrators usually have pretty interesting things saved. 
```
search -f flag3.txt
Found 1 result...
    c:\Users\Jon\Documents\flag3.txt (37 bytes)

flag{admin_documents_can_be_valuable}
```
