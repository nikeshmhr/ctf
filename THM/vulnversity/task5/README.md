# Privilege Escalation

## Notes

```

```

## Questions

1. On the system, search for all SUID files. What file stands out?

```
find / -user root -perm -4000 -exec ls -ldb {} \;

/bin/systemctl
```

2. Become root and get the last flag (/root/root.txt)

```
gtfobins

a58ff8579f0a9270368d33a9966c7fd5
```
