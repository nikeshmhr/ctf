# Research - Analyse the code

## Questions
1. What's the default hash for the backdoor?
```
look at the backdoor go source
bdd04d9bb7621687f5df9001f5098eb22bf19eac4c2c30b6f23efed4d24807277d0f8bfccb9e77659103d78c56e66d2d7d8391dfc885d0e9b68acd01fc2170e3
```

2. What's the hardcoded salt for the backdoor?
```
same as #1
1c362db832f3f864c8c2fe05f2002a05
```

3. What was the hash that the attacker used? - go back to the PCAP for this!
```
6d05358f090eea56a238af02e47d44ee5489d234810ef6240280857ec69712a3e5e370b8a41899d0196ade16c0d54327c5654019292cbfe0b5e98ad1fec71bed
```

4. Crack the hash using rockyou and a cracking tool of your choice. What's the password?
```
hashcat password:hash crack
november16
```