# The basics - An Intro to WPA

## Notes
Key Terms
* SSID: The network "name" that you see when you try and connect
* ESSID: An SSID that *may* apply to multiple access points, eg a company office, normally forming a bigger network. For Aircrack they normally refer to the network you're attacking.
* BSSID: An access point MAC (hardware) address
* WPA2-PSK: Wifi networks that you connect to by providing a password that's the same for everyone
* WPA2-EAP: Wifi networks that you authenticate to by providing a username and password, which is sent to a RADIUS server.
* RADIUS: A server for authenticating clients, not just for wifi.

The core of WPA2 is 4 way handshake. The 4 way handshake allows the client and AP to both prove that they know the key, without telling each other.

The keys for WPA are derived from both the ESSID and the password for the network. The ESSID acts as a salt, making dictionary attacks more difficult. It means that for a given password, the key will still vary for each access point. This means that unless you precompute the dictionary for just that access point/MAC address, you will need to try passwords until you find the correct one.


## Questions
1. What type of attack on the encryption can you perform on WPA(2) personal?
```
brute force
```

2. Can this method be used to attack WPA2-EAP handshakes? (Yea/Nay)
```
Nay
```

3. What three letter abbreviation is the technical term for the "wifi code/password/passphrase"?
```
PSK
```

4. What's the minimum length of a WPA2 Personal password?
```
8
```