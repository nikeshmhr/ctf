# [Section 5 - SQL Injection]: sqlmap

## Notes
https://github.com/sqlmapproject/sqlmap/wiki/Usage

For manual injection https://owasp.org/www-community/attacks/SQL_Injection

## Questions
1. How do you specify which url to check?
```
-u
```

2. What about which google dork to use?
```
-g
```

3. How do you select(lol) which parameter to use?(Example: in the url http://ex.com?test=1 the parameter would be test.)
```
-p
```

4. What flag sets which database is in the target host's backend?(Example: If the flag is set to mysql then sqlmap will only test mysql injections).
```
--dbms
```

5. How do you select the level of depth sqlmap should use(Higher = more accurate and more tests in general).
```
--level
```

6. How do you dump the table entries of the database?
```
--dump
```

7. Which flag sets which db to enumerate?
```
-d
```

8. Which flag sets which table to enumerate?
```
-t
```

9. Which flag sets which column to enumerate?
```
-c
```

10. How do you ask sqlmap to try to get an interactive os-shell?
```
--os-shell
```

11. What flag dumps all data from every table
```
--dump-all
```