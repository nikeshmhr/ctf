# The TCP/IP model

## Notes
* Similar to OSI model, few years older and serves as the basis for real-world networking
* Has four layers: Application, Transport, Internet and Network Interface]

    | TCP/IP |
    |----|
    |Application|
    |Transport|
    |Internet|
    |Network Interface|

Two models match up like this:

![](https://muirlandoracle.co.uk/wp-content/uploads/2020/02/image-3.png)

### TCP
* _connection-based_ protocol
* Before sending any data via TCP, you must first form a stable connection between the two computers.
* The process of forming this connection is called the _three-way handshare_

### 3 way handshake
* When you attempt to make a connection, your computer first sends a special request to the remote server indicating that it wants to initialise a connection. This request contains something called _SYN_ (synchronise) bit, which makes first contact in starting the connection process.
* The server will then respond with a packet containing the SYN bit, as well as another "acknowledgement" bit, called _ACK_.
* Finally, your computer will send a packet that contains the ACK bit by itself, confirming that the connection has been setup successfully.
* With the 3-way handshake successfully completed, data can be reliably transmitted between the two computers.
* Any data that is lost or corrupted on transmission is re-sent, leading to a connection which appears to be lossless.
![](https://muirlandoracle.co.uk/wp-content/uploads/2020/03/image-2.png)


## Questions
1. Which model was introduced first, OSI or TCP/IP?
```
TCP/IP
```

2. Which layer of the TCP/IP model covers the functionality of the Transport layer of the OSI model (Full Name)?
```
transport
```

3. Which layer of the TCP/IP model covers the functionality of the Session layer of the OSI model (Full Name)?
```
application
```

4. The Network Interface layer of the TCP/IP model covers the functionality of two layers in the OSI model. These layers are Data Link, and?.. (Full Name)?
```
physical
```

5. Which layer of the TCP/IP model handles the functionality of the OSI network layer?
```
internet
```

6. What kind of protocol is TCP?
```
connection-based
```

7. What is SYN short for?
```
synchronise
```

8. What is the second step of the three way handshake?
```
SYN/ACK
```

9. What is the short name for the "Acknowledgement" segment in the three-way handshake?
```
ACK
```
