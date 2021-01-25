#  If Statements

## Notes
The general format of an if statement is:
```
if(condition) {
    //dostuff
} else if(condition) {
    // do stuff
} else {
    // do it
}
```

If statement uses 3 important instructions in assembly:
* `cmpq source2, source1`: it is like computing a-b without setting destination
* `testq source2, source1`: it is like computing a&b without setting destination

The following questions involve analysing the if2 binary.
## Questions
1. What is the value of var_8h before the popq and ret instructions?
```
96
```

2. what is the value of var_ch before the popq and ret instructions?
```
0
```

3. What is the value of var_4h before the popq and ret instructions?
```
1
```

4. What operator is used to change the value of var_8h, input the symbol as your answer(symbols include +, -, *, /, &, |):
```
&
```