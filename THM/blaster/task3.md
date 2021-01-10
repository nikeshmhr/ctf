# Breaching the Control Room


## Questions
1. When enumerating a machine, it's often useful to look at what the user was last doing. Look around the machine and see if you can find the CVE which was researched on this server. What CVE was it?
```
CVE-2019-1388
```

2. Looks like an executable file is necessary for exploitation of this vulnerability and the user didn't really clean up very well after testing it. What is the name of this executable?
```
hhupd
```

3. Now that we've spawned a terminal, let's go ahead and run the command 'whoami'. What is the output of running this?
```
nt authority\system
```

4. Now that we've confirmed that we have an elevated prompt, read the contents of root.txt on the Administrator's desktop. What are the contents? Keep your terminal up after exploitation so we can use it in task four!
```
THM{COIN_OPERATED_EXPLOITATION}
```
