# You're being watched - Capturing packets to attack

## Notes
https://linuxhint.com/install_aircrack-ng_ubuntu/
https://www.aircrack-ng.org/doku.php?id=install_aircrack
https://www.aircrack-ng.org/doku.php?id=airmon-ng


## Questions
1. How do you put the interface “wlan0” into monitor mode with Aircrack tools? (Full command)
```
airmon-ng start wlan0
```

2. What is the new interface name likely to be after you enable monitor mode?
```
wlan0mon
```

3. What do you do if other processes are currently trying to use that network adapter? 
```
airmon-ng check kill
```

4. What tool from the aircrack-ng suite is used to create a capture?
```
airodump-ng
```

5. What flag do you use to set the BSSID to monitor?
```
--bssid
```

6. And to set the channel?
```
--channel
```

7. And how do you tell it to capture packets to a file?
```
-w
```