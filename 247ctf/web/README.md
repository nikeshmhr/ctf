# Secured Session

## Notes
```
If you can guess our random secret key, we will tell you the flag securely stored in your session.
```

Using `session` cookie value to decode with jwt.io gives some base64 string. Decoding that base64 string gives the flag.


# Trusted Client

## Notes
```
Developers don't always have time to setup a backend service when prototyping code. Storing credentials on the client side should be fine as long as it's obfuscated right?
```

Copy the function definition and assign it to some variable in chrome developer console. And then print out the function definition by typing recently created variable name. You'll see the code in normal deobfuscated javascript.


# Compare The Pair

## Notes
```
Can you identify a way to bypass our login logic? MD5 is supposed to be a one-way function right?
```

We are provided with hash (0e902564435691274142490923013038) and salt (f789bbc328a3d1a3). We can bruteforce password using hashcat.
Creating hash file in the format `hash:salt`. [Reference](https://hashcat.net/wiki/doku.php?id=example_hashes)

`0e902564435691274142490923013038:f789bbc328a3d1a3` => Doesn't work

Hash is being compared loosely which we can take advantage of https://www.whitehatsec.com/blog/magic-hashes/
In php this condition passes:
```php
if("0e111111111111111111112222222222" == "0e902564435691274142490923013038")
```

We have to find a hash that starts with `0e` and all other 30 charcters must be numeric. To do that we need to use `rockyou.txt` to generate md5 for each word using given salt and check if generated hash starts with `0e` and after that has digits only no alphabets. [Script](magic-hash-generator.py)


# Acid Flag Bank

## Notes
```
You can purchase a flag directly from the ACID flag bank, however there aren't enough funds in the entire bank to complete that transaction! Can you identify any vulnerabilities within the ACID flag bank which enable you to increase the total available funds?
```

References:

* https://github.com/TheHackerDev/race-the-web
* https://www.youtube.com/watch?v=bhHvT788juk&ab_channel=247CTF
* https://stackoverflow.com/questions/9624967/how-do-i-use-curl-to-perform-multiple-simultaneous-requests

Exploit race condition while checking balance before transfer. [Script](acid-bank-race-condition.py)


# Forgotten Flag Pointer

## Notes
```
We have opened the flag, but forgot to read and print it. Can you access it anyway?
```

From the source it looks like we have to bypass conditional check.

`strlen` [docs](https://www.php.net/manual/en/function.strlen.php) has a notes which says if array is passed it result in `NULL`. If we pass `[]` as param length check will be `true`

Following statement is true:
```php
NULL <= 10
```

How to pass length check as well as refer to /tmp/flag.txt file?
* eval(\$fp)

Turns out the code syntax itself doesn't have any vulnerability. But the fact that in linux everything is a file make this solution for this challenge interesting. We can use file descriptor to enumerate contents of `/dev/flag.txt`. File descriptors are at `/dev/fd/#`, which gives us from 0 to 99 numbered files to enumerate. [Script](file-descriptor-reader.py)

[Reference](https://hackmd.io/@Chivato/rkj-Y1GVI)


# Slippery Upload

## Notes
```
Can you abuse the zip upload and extraction service to gain code execution on the server?
```

```python
from flask import Flask, request
import zipfile, os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = '/tmp/uploads/'

@app.route('/')
def source():
    return '
%s
' % open('/app/run.py').read()

def zip_extract(zarchive):
    with zipfile.ZipFile(zarchive, 'r') as z:
        for i in z.infolist():
            with open(os.path.join(app.config['UPLOAD_FOLDER'], i.filename), 'wb') as f:
                f.write(z.open(i.filename, 'r').read())

@app.route('/zip_upload', methods=['POST'])
def zip_upload():
    try:
        if request.files and 'zarchive' in request.files:
            zarchive = request.files['zarchive']
            if zarchive and '.' in zarchive.filename and zarchive.filename.rsplit('.', 1)[1].lower() == 'zip' and zarchive.content_type == 'application/octet-stream':
                zpath = os.path.join(app.config['UPLOAD_FOLDER'], '%s.zip' % os.urandom(8).hex())
                zarchive.save(zpath)
                zip_extract(zpath)
                return 'Zip archive uploaded and extracted!'
        return 'Only valid zip archives are acepted!'
    except:
         return 'Error occured during the zip upload process!'

if __name__ == '__main__':
    app.run()
```

Can take advantage of file name.

https://b4d.sablun.org/blog/2020-05-06-247ctf-com-web-slippery-upload/
https://snyk.io/research/zip-slip-vulnerability

To Create Zip will ../ paths
https://raw.githubusercontent.com/ptoomey3/evilarc/master/evilarc.py