# Web Exploitation: The Elf Strikes Back!

## Notes
```
localIP: 10.9.18.129
10.10.73.154
```

## Questions
1. What string of text needs adding to the URL to get access to the upload page?
```
?id=ODIzODI5MTNiYmYw
```

2. What type of file is accepted by the site?
```
image
```

3. In which directory are the uploaded files stored?
```
/uploads/
```

4. What is the flag in /var/www/flag.txt?
```
filter bypass using file extension file.png.php where this file is reverse shell
THM{MGU3Y2UyMGUwNjExYTY4NTAxOWJhMzhh}
```