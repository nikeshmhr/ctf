# Elfcryption

## Notes

```
unzip file
```

## Questions

1. What is the md5 hashsum of the encrypted note1 file?

```
md5sum note1.txt.gpg gives md5 hashsum

24cf615e2a4f42718f2ff36b35614f8f
```

2. WHere was elf Bob told to meet Alice?

```
gpg -d note1.txt.gpg with passphrase 25daysofchristmas

Santa's Grotto
```

3. Decrypt note2 and obtain the flag!

```
openssl rsautl -decrypt -inkey private.key -in note2_encrypted.txt -out plaintext.txt with passphrase hello

THM{ed9ccb6802c5d0f905ea747a310bba23}
```
