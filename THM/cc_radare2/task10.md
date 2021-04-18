# Write mode

## Notes
Occasionally you might end up in a situation where a task is impossible to solve with the current instructions. For example take this code 
```C
int val = 4;
if(val == 5) {
    printf("%s","You win!");
}
```
You will never be able to get it to print out You win! because under normal circumstances val will never be set equal to 5. This is where write mode comes in, it allows you to change instructions so you can get certain conditions to execute. All commands involving write mode start with `w`

Binary patching to complete `example4`. Seek to address `s <ADD>`, patch it `wx OPCODE`


## Questions
1. How do you write a string to the current memory address.
```
w
```

2. What command lists all write changes?
```
wc
```

3. What command modifies an instruction at the current memory address?
```
wa
```