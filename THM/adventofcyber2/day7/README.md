# Networking: The Grinch Really Did Steal Christmas

## Learning Objectives
-   IP Addresses and their assignment.
-   Understanding TCP/IP and UDP
    -   3-way handshake
-   Wireshark Crash Course (where is it used and why)
    -   Basic filtering and operators
-   Analysing our first few PCAPS
    -   HTTP
    -   SMB

## Notes
```
```

## Questions
1. Open "pcap1.pcap" in Wireshark. What is the IP address that initiates an ICMP/ping?
```
10.11.3.2
```

2. Open "pcap1.pcap" in Wireshark. What is the IP address that initiates an ICMP/ping?
```
http.request.method == get
```

3. Now apply this filter to "pcap1.pcap" in Wireshark, what is the name of the article that the IP address "10.10.67.199" visited?
```
reindeer-of-the-week
```

4. Let's begin analysing "pcap2.pcap". Look at the captured FTP traffic; what password was leaked during the login process?
There's a lot of irrelevant data here - Using a filter here would be useful!
```
plaintext_password_fiasco
```

5. Continuing with our analysis of "pcap2.pcap", what is the name of the protocol that is encrypted?
```
ssh
```

6. Analyse "pcap3.pcap" and recover Christmas!
What is on Elf McSkidy's wishlist that will be used to replace Elf McEager?
```
```