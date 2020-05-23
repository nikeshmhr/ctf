# Elf Applications

## Notes

export IP=10.10.65.116

```
Not shown: 995 closed ports
PORT     STATE SERVICE
21/tcp   open  ftp
22/tcp   open  ssh
111/tcp  open  rpcbind
2049/tcp open  nfs
3306/tcp open  mysql
```

## Questions

1. What is the password inside the creds.txt file?

```
showmount -e ip
mount ip:/opt/files ./files
securepassword123
```

2. What is the name of the file running on port 21?

```
login using anonymous:anonymous
file.txt
```

3. What is the password after enumerating the database?

```
file.txt from #2 contains mysql creds
creds: admin:bestpassword
```
