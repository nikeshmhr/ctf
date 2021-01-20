# [Section 5: Advanced File Operations]: chown

## Notes
`chown` allows to change the user and group of any file. 

The syntax for chown is: `chown user:group file`

Note: You can only use chown if you are "above" that other user, meaning that chown is best done with the root(administrator) user.
You can also use chown without specifying a group. So you can just use chown user file if you only wanted to change the user but keep the group.

## Questions
1. How would you change the owner of file to paradox
```
chown paradox file
```

2. What about the owner and the group of file to paradox
```
chown paradox:paradox file
```

3. What flag allows you to operate on every file in the directory at once?
```
-R
```
