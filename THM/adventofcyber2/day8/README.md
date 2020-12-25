# Networking: What's Under the Christmas Tree?


## Notes
```
```

## Nmap
- Host discovery
- Vulnerability discovery
- Service/Application discover
- Connect Scan `nmap -sT <ip>`
- SYN Scan `nmap -sS <ip>`

### Nmap Timing Templates
- Uses to determine Nmap's performance
- Measured in aggressiveness, can use one of six profiles [0 to 5]
- `-T0` being the stealthiest, scans one port every 5 minutes
- `-T5` is most aggressive and potential to be inaccurate because it waits 0.3 seconds for remote to respond to a handshake

### Nmap's Scripting Engine
-   Using scripts to automate various actions: Exploitation, Fuzzing, Bruteforcing
-   Scripts can be found [here](https://nmap.org/nsedoc/scripts/)
-   Usage: `nmap --script ftp-proftpd-backdoor -p 21 <ip>`

### Additional Scan Types
Flag|Usage Example|Description
----|-------------|-----------
-A|`nmap -A <ip>`|Scan the host to identify services running by matching against Namp's database with OS detection
-O|`nmap -O <ip>`|Scan the host to retrieve and perform OS detection
-p|`nmap -p 22 <ip>`|Scan a specific port number on the host. A range of ports can also be provided(i.e. 10-100) by using the first and last value of the range like so: `nmap -p 10-100 <ip>`
-p-|`nmap -p- <ip>`|Scan all ports(0-65535) on the host
-sV|`nmap -sV <ip>`|Scan the host using TCP and perform version fingerprinting

## Questions
1. When was Snort created?
```
1998
```

2. Using Nmap on MACHINE_IP , what are the port numbers of the three services running?  (Please provide your answer in ascending order/lowest -> highest, separated by a comma)
```
PORT     STATE    SERVICE
80/tcp   open     http
2222/tcp open     EtherNetIP-1
3389/tcp open     ms-wbt-server
3971/tcp filtered lanrevserver

80,2222,3389
```

3. Use Nmap to determine the name of the Linux distribution that is running, what is reported as the most likely distribution to be running?
```
ubuntu
```

4. Use Nmap's Network Scripting Engine (NSE) to retrieve the "HTTP-TITLE" of the webserver. Based on the value returned, what do we think this website might be used for?
```
nmap -sC -sV -p 80 <ip>
blog
```