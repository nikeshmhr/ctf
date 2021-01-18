# [Section 4 - Hash Cracking]: hashcat

## Notes
A full list of all modes can be found [here](https://hashcat.net/wiki/doku.php?id=example_hashes).
https://hashcat.net/wiki/doku.php?id=hashcat


## Qustions
1. What flag sets the mode.
```
-m
```

2. What flag sets the "attack mode"
```
-a
```

3. What is the attack mode number for Brute-force    
```
3
```

4. What is the mode number for SHA3-512    
```
17600
```

5. Crack This Hash:56ab24c15b72a457069c5ea42fcfc640
Type: MD5
```
hashcat -m 0 56ab24c15b72a457069c5ea42fcfc640 rockyou.txt
happy
```

6. Crack this hash:4bc9ae2b9236c2ad02d81491dcb51d5f
Type: MD4
```
hashcat -m 900 4bc9ae2b9236c2ad02d81491dcb51d5f rockyou.txt
nootnoot
```