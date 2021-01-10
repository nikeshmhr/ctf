# Activate Forward Scanners and Launch Proton Torpedoes

## Notes
```
```

## Questions
1. How many ports are open on our target system?
```
PORT     STATE SERVICE
80/tcp   open  http
3389/tcp open  ms-wbt-server

2
```

2. Looks like there's a web server running, what is the title of the page we discover when browsing to it?
```
iis windows server
```

3. Interesting, let's see if there's anything else on this web server by fuzzing it. What hidden directory do we discover?
```
/retro
```

4. Navigate to our discovered hidden directory, what potential username do we discover?
```
wade
```

5. Crawling through the posts, it seems like our user has had some difficulties logging in recently. What possible password do we discover?
```
ready player one post

parzival
```

6. Log into the machine via Microsoft Remote Desktop (MSRDP) and read user.txt. What are it's contents?
```
THM{HACK_PLAYER_ONE}
```
