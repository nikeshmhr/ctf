# Flag Submission

## Notes
```
doesn't require ssh bruteforcing
```

## Questions
1. user.txt
```
thm.jpg
magic bytes for jpg

reveals hidden directory
/th1s_1s_h1dd3n

bruteforce secret param => 73

steghide extract -sf thm.jpg (using password)
rot10 username

steghide on another image to reveal password
*axA&GF8dP

THM{d5781e53b130efe2f94f9b0354a5e4ea}
```

2. root.txt
```
linpeas
local priviledge escalation for screen 4.5.0
THM{5ecd98aa66a6abb670184d7547c8124a}
```