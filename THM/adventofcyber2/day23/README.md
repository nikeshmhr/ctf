# Blue Teaming The Grinch strikes again!

## Notes
```
{7a9eea15-0000-0000-0000-010000000000}
```

## Questions
1. Decrypt the fake 'bitcoin address' within the ransom note. What is the plain text value?
```
nomorebestfestivalcompany
```

2. At times ransomware changes the file extensions of the encrypted files. What is the file extension for each of the encrypted files?
```
.grinch
```

3. What is the name of the suspicious scheduled task?
```
opidsfsdf
```

4. Inspect the properties of the scheduled task. What is the location of the executable that is run at login?
```
C:\User\Administrator\Desktop\opidsfsdf.exe
```

5. There is another scheduled task that is related to VSS. What is the ShadowCopyVolume ID?
```
{7a9eea15-0000-0000-0000-010000000000}
```

6. Assign the hidden partition a letter. What is the name of the hidden folder?
```
confidential
```

7. Right-click and inspect the properties for the hidden folder. Use the 'Previous Versions' tab to restore the encrypted file that is within this hidden folder to the previous version. What is the password within the file?
```
m33pa55w0rdIZseecure!
```