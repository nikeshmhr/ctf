# Aircrack-ng - Let's Get Cracking

## Notes
Crack capture
Useful Information

BSSID: 02:1A:11:FF:D9:BD

ESSID: 'James Honor 8'

https://www.aircrack-ng.org/doku.php?id=aircrack-ng

convert cap to hccapx
https://hashcat.net/cap2hccapx/


## Questions
1. What flag do we use to specify a BSSID to attack?
```
-b
```

2. What flag do we use to specify a wordlist?
```
-w
```

3. How do we create a HCCAPX in order to use hashcat to crack the password?
```
-j
```

4. Using the rockyou wordlist, crack the password in the attached capture. What's the password?
```
convert capture file to hccapx
hashcat.exe -m 2500 capture.hccapx rockyou.txt

greeneggsandham
```

5. Where is password cracking likely to be fastest, CPU or GPU?
```
GPU
```