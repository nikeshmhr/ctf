# Web Exploitation: A Christmas Crisis

## Notes
```
10.10.164.7
```

## Questions
1. What is the name of the cookie used for authentication?
```
auth
```

2. In what format is the value of this cookie encoded?
```
7b22636f6d70616e79223a22546865204265737420466573746976616c20436f6d70616e79222c2022757365726e616d65223a2261646d696e227d => {"company":"The Best Festival Company", "username":"admin"}
hexadecimal
```

3. Having decoded the cookie, what format is the data stored in?
```
json
```

4. Figure out how to bypass the authentication. What is the value of Santa's cookie?
```
{"company":"The Best Festival Company", "username":"admin"} to hex
7b22636f6d70616e79223a22546865204265737420466573746976616c20436f6d70616e79222c2022757365726e616d65223a2273616e7461227d
```

5. What is the flag you're given when the line is fully active?
```
activate all services
THM{MjY0Yzg5NTJmY2Q1NzM1NjBmZWFhYmQy}
```