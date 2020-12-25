# Web Exploitation: Santa's watching

## Notes
```
```

## Questions
1. Given the URL "http://shibes.xyz/api.php", what would the entire wfuzz command look like to query the "breed" parameter using the wordlist "big.txt" (assume that "big.txt" is in your current directory)

Note: For legal reasons, do not actually run this command as the site in question has not consented to being fuzzed!
```
wfuzz -c -z file,big.txt -d “breed=FUZZ” -u http://shibes.xyz/api.php
```

2. Use GoBuster (against the target you deployed -- not the shibes.xyz domain) to find the API directory. What file is there?
```
/api dir
site-log.php
```

3. Fuzz the date parameter on the file you found in the API directory. What is the flag displayed in the correct post?
```
date=20201125
THM{D4t3_AP1}
```