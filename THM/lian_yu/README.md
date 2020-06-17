# Lian_Yu

## Notes

```
export IP=10.10.219.14
dirsearch
[21:18:33] 301 -  235B  - /island  ->  http://10.10.219.14/island/
    [21:24:07] 301 -  240B  - /island/2100  ->  http://10.10.219.14/island/2100/
        [21:39:47] 200 -   71B  - /island/2100/green_arrow.ticket

Puzzel Piece:
/island has a codeword vigilante
```

## Questions

2. What is the Web Directory you found?

```
Hint: In Numbers
search for numbers in /island and found 2100

2100
```

3. what is the file name you found?

```
after visiting /island/2100 there's a comment:
<!-- you can avail your .ticket here but how?   -->
.ticket could be our extension so lets dirsearch file in directory /island with extension .ticket
dirsearch -u domain/island/2100 -e ticket -w wordlist -f

/green_arrow.ticket


```

4. what is the FTP Password?

```
content of /green_arrow.ticket
cyberchef decodes to base58

!#th3h00d
```

5. what is the file name with SSH password?

```
connect ftp using vigilante:!#th3h00d
ftp ip
ls -al
drwxr-xr-x    2 1001     1001         4096 May 05 11:10 .
drwxr-xr-x    4 0        0            4096 May 01 05:38 ..
-rw-------    1 1001     1001           44 May 01 07:13 .bash_history
-rw-r--r--    1 1001     1001          220 May 01 05:38 .bash_logout
-rw-r--r--    1 1001     1001         3515 May 01 05:38 .bashrc
-rw-r--r--    1 0        0            2483 May 01 07:07 .other_user
-rw-r--r--    1 1001     1001          675 May 01 05:38 .profile
-rw-r--r--    1 0        0          511720 May 01 03:26 Leave_me_alone.png
-rw-r--r--    1 0        0          549924 May 05 11:10 Queen's_Gambit.png
-rw-r--r--    1 0        0          191026 May 01 03:25 aa.jpg

the most obvious file Leave_me_alone.png was wrongly formatted.
replace first 8 byte of data with png magic headers and fix 12th byte to 00
the image gives us password "password"
use steghide extract -sf aa.jpg with the password gives us zip file.
inside the zip is a file shado with password

shado

```

6. user.txt

```
username from .other_users text coz vigilante doesn't work
ssh into box with ssh creds => slade:M3tahuman

THM{P30P7E_K33P_53CRET5__C0MPUT3R5_D0N'T}
                        --Felicity Smoak
```

7. root.txt

```
sudo -l
search for gtfobin pkexec
THM{MY_W0RD_I5_MY_B0ND_IF_I_ACC3PT_YOUR_CONTRACT_THEN_IT_WILL_BE_COMPL3TED_OR_I'LL_BE_D34D}
```
