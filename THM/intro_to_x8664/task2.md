# Introduction

## Notes
Computers execute machine code, which is encoded as bytes, to carry out tasks on a computer. Before an executable file is produced, the source code is first compiled into assembly(.s files), after which the assembler converts it into an object program(.o files), and operations with a linker finally make it an executable.

`r2 -d binary` opens the binary in debugging mode

`pdf @main` means print disassembly function

First column contains the memory address of the instruction, which are usually stored in a structure called the stack.
The middle column contains the instructions encoded in bytes (which is usually the machine code).
And the last column contains the humable readable instructions.

The core of assembly language involves using registers to do following:
* Transfer data between memory and register and vice-versa
* Perform arithmetic operations on registers and data
* Transfer control to other parts of the program

The `rsp` is the stack pointer and it points to the top of the stack which contains the most recent memory address. The stack is the data structure that manages memory for the programs.

The `rbp` is a frame pointer  and points to the frame of the function currently being executed - every function is executed in a new frame. To move data using registers, the following instruction is used:

`movq source, destination`