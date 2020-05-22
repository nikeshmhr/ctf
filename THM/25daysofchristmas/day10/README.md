# Metasploit

-   A pentest framework, allows to choose explit and payload and execute against a target.
-   Comes with many other tools like MSFVenom to create custom shellcode (which when executed will give you shell on target machine)

## Questions

1. Compromise the web server using Metasploit. What is flag1?

```
THM{3ad96bb13ec963a5ca4cb99302b37e12}
msf, CVE-2017-5638, reverse_shell_tcp, meterpreter to shell spawn find / 2>/dev/null |grep -i "flag1"
```

2. Now you've compromised the web server, get onto the main system. What is Santa's SSH password?

```
santa:rudolphrednosedreindeer
find / 2>/dev/null | grep -i "ssh"
```

3. Who is on line 148 of the naughty list?

```
Melisa Vanhoose
ssh using creds from #2
read file: cat -n filename // gives linenumber
```

4. Who is on line 52 of the nice list?

```
Lindsey Gaffney
```
