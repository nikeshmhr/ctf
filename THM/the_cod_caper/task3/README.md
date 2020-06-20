# Web Enumration

## Notes

wordlist to use [big.txt](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/big.txt)

## Questions

1. What is the name of the important file on the server?

```
dirsearch.py -w ./big.txt -u http://10.10.70.35/ -f -e=html,php,txt -t 64

administrator.php
```
