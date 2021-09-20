# Scan Types: TCP Connect Scans

`-sT`

## Notes

### Understanding TCP 3 way handshake

3 way handshake consists of three stages

-   First the connecting system sends a TCP request to the target sever with the SYN flag set.
-   The sever then acknowledges this packet with a TCP response containing the SYN flag, as well as the ACK flag.
-   Finally, our system completes the handshake by sending a TCP request with the ACK flag set.

![Flow](https://muirlandoracle.co.uk/wp-content/uploads/2020/03/image-2.png)

It relates to nmap because the TCP Connect Scans work by performing 3 way handshake with each target port in turn. Nmap tries to connect to each specified TCP port, and determines whether the service is open by response it receives.

## Questions

1. Which RFC defines the appropriate behaviour for the TCP protocol?

```
RFC 793
```

2. If a port is closed, which flag should the server send back to indicate this?

```
RST
```
