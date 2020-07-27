# Section 1 - Network Utilities - nmap

## Notes

```
map scan report for 10.10.177.126
Host is up (0.30s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
```

## Questions

3. How do you do a "ping scan"(just tests if the host(s) is up)?

```
-sn
```

4. What is the flag for a UDP scan?

```
-sU
```

5. How do you run default scripts?

```
-sC
```

6. How do you enable "aggressive mode"(Enables OS detection, version detection, script scanning, and traceroute)

```
-A
```

7. What flag enables OS detection

```
-O
```

8. How do you get the versions of services running on the target machine

```
-sV
```

10. How many ports are open on the machine?

```
1
```

11. What service is running on the machine?

```
apache
```

12. What is the version of the service?

```
2.4.18
```

13. What is the output of the http-title script(included in default scripts)

```
Apache2 Ubuntu Default Page: It works
```
