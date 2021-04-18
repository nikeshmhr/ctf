#  Debugging

## Notes
Recall that in the task "Command Line Options" you learned that the -d flag has radare enter debug mode. Debug mode allows you to set breakpoints and offers a lot of options to not only navigate through your binary, but to analyze the data that goes in and out of the registers as well.


## Questions
1. How do you set a breakpoint?
```
dx
```

2. What command is used to print out the values of all the registers?
```
dr
```

3. How do you run through the program until the program either ends or you hit the next breakpoint?
```
dc
```

4. What if you want to step through the binary one line at a time?
```
ds
```

5. How do you go forth 2 lines in the binary?
```
ds 2
```

6. How do you list out the indexes and memory addresses of all breakpoints?
```
dbi
```