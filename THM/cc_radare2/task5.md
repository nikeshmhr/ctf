# Navigating Through Memory

## Notes
`s` is the command that is used to navigate through the memory of your binary. With it and its variations you can you can get information about where you are in the binary as well as move to different points in the binary.


## Questions
1. How do you print out the the current memory address your located at in the binary?
```
s
```

2. What command do you use to go to a specific point in memory with the syntax `<command> <address>`?
```
s
```

3. What command would you run to go 5 bytes forward?
```
s+ 5
```

4. What about 12 bytes backward?
```
s- 12
```

5. How do you undo the previous seek?
```
s-
```

6. How would you go to the memory address of the main function?
```
s main
```

7. What if you wanted to go to the address of the rax register?
```
sr rax
```