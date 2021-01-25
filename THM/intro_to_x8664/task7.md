# crackme2

## Notes
e asm.syntax=intel
db 0x5568721f08af


var_3ch has file input?

## Question
1. What is the correct password?
```
db after cmp dl, al
extract one character at a time

better approache would be to db at wrong password lea, so when we reach there we can say that last chr comparison failed and look at our register value drr and extract actual char

dwperuc3s
```