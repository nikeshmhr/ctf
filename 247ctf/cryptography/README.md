# My Magic Bytes

## Notes
```
Can you recover the secret XOR key we used to encrypt the flag?
```

`file` commands says it's a jpg file. List of jpg magic bytes:
1. FF D8 FF DB
2. FF D8 FF E0 00 10 4A 46 49 46 00 01
3. FF D8 FF EE

First 16 bytes of encrypted file:
B9 14 06 45 71 E0 B5 F7 37 07 CB 85 47 CC F9

Doing xor for each possible magic bytes to find all possible keys:
1. FF D8 FF DB (XOR) B9 14 06 45 => 46ccf99e
2. FF D8 FF E0 00 10 4A 46 49 46 00 01 (XOR) B9 14 06 45 71 E0 B5 F7 37 07 CB 85 => 46ccf9a571f0ffb17e41cb84
3. FF D8 FF EE (XOR) B9 14 06 45 => 46ccf9ab

XOR file using cyberchef with all possible keys