# Printing

## Notes
* `p` is a command that shows data in a myriad of formats.
* The command is useful for when you want to get information about what is happening in memory, and get some of the data that's contained in memory as well. 
* With the `p` command it is also useful to know about the `@` symbol in radare.
* The `@` symbol is used to specify that something is an address in memory, for example if you wanted to specify you were talking about the memory address of the main function you would use `<command> @main`

## Questions
1. How would you print the hex output of where you currently are in memory?
```
px
```

2. How would you print the disassembly of where you're currently at in memory?
```
pd
```

3. What if you wanted the disassembly of the main function?
```
pd @ main
```

4. What command prints out the emoji hexdump? (this is not useful at all I just find it funny)
```
pxe
```

5. What if you decided you were too good for rows and you wanted the disassembly in column format?
```
pC
```

6. What is the value of the first variable in the main function for the example 3 binary?
```
1
```

7. What about the second variable?
```
5
```