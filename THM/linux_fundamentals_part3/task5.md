# [Section 5 - Advanced File Operations]: find

## Notes
The true power of this command though comes from the parameters you can provide it. You can use `find dir -user` , to list every file owned by a specific user; you can use `find dir -group` to list every file owned by a specific group. The sheer customizability of the command is it's most powerful feature.

## Questions
1. How do you find files that have specific permissions?
```
-perm
```

2. How would you find all the files in /home
```
find /home
```

3. How would you find all the files owned by paradox on the whole system
```
find / -user paradox
```