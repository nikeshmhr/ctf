# Practical

## Notes

```
Starting Nmap 7.60 ( https://nmap.org ) at 2021-09-20 20:21 +0545
Nmap scan report for 10.10.58.127
Host is up (0.26s latency).
Not shown: 995 filtered ports
PORT     STATE SERVICE
21/tcp   open  ftp
53/tcp   open  domain
80/tcp   open  http
135/tcp  open  msrpc
3389/tcp open  ms-wbt-server
```

## Questions

1. Does the target (`10.10.58.127`)respond to ICMP (ping) requests (Y/N)?

```
nmap -PM <IP>

N
```

2. Perform an Xmas scan on the first 999 ports of the target -- how many ports are shown to be open or filtered?

```
sudo nmap -Pn -sX -p1-999 10.10.58.127
999
```

3. There is a reason given for this -- what is it?
   Note: The answer will be in your scan results. Think carefully about which switches to use -- and read the hint before asking for help!

```
no response
```

4. Perform a TCP SYN scan on the first 5000 ports of the target -- how many ports are shown to be open?

```
5
```

5. Deploy the `ftp-anon` script against the box. Can Nmap login successfully to the FTP server on port 21? (Y/N)

```
nmap --script=ftp-anon -p21 <IP> -vv
Y
```
