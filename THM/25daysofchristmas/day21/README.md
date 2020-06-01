# Reverse Elf-ineering

```
binary stuff
```

## Notes

```

```

## Questions

1. What is the value of local_ch when its corresponding movl instruction is called(first if multiple)?

```
r2 -d challenge1
aa
afl | grep main
pdf @main
db first_movl (for local_ch)
dc (run)
pdf
px @add (address of local_ch)
ds (exe next instruction)
px @add (address of local_ch)
you'll see first byte is 1

1
```

2. What is the value of eax when the imull instruction is called?

```
add breakpoint after imul instruction
dr (to display registers)

6
```

3. What is the value of local_4h before eax is set to 0?

```
set breakpoint before mov eax, 0
px @address (address of local_4h)

6
```
