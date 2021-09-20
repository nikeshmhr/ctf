# Nmap Switches

## Notes

## Questions

1. What is the first switch listed in the help menu for a 'Syn Scan' (more on this later!)?

```
-sS
```

2. Which switch would you use for a "UDP scan"?

```
-sU
```

3. If you wanted to detect which operating system the target is running on, which switch would you use?

```
-O
```

4. Nmap provides a switch to detect the version of the services running on the target. What is this switch?

```
-sV
```

5. The default output provided by nmap often does not provide enough information for a pentester. How would you increase the verbosity?

```
-vv or more for greater effect
-v
```

6. Verbosity level one is good, but verbosity level two is better! How would you set the verbosity level to two?
   (Note: it's highly advisable to always use at least this option)

```
-vv
```

7. What switch would you use to save the nmap results in three major formats?

```
-oA
```

8. What switch would you use to save the nmap results in a "normal" format?

```
-oN
```

9. A very useful output format: how would you save results in a "grepable" format?

```
-oG
```

10. Sometimes the results we're getting just aren't enough. If we don't care about how loud we are, we can enable "aggressive" mode. This is a shorthand switch that activates service detection, operating system detection, a traceroute and common script scanning. How would you activate this setting?

```
-A
```

11. Nmap offers five levels of "timing" template. These are essentially used to increase the speed your scan runs at. Be careful though: higher speeds are noisier, and can incur errors! How would you set the timing template to level 5?

```
-T5
```

12. We can also choose which port(s) to scan. How would you tell nmap to only scan port 80?

```
-p 80
```

13. How would you tell nmap to scan ports 1000-1500?

```
-p 1000-1500
```

14. How would you tell nmap to scan all ports?

```
-p-
```

15. How would you activate a script from the nmap scripting library (lots more on this later!)?

```
--script
```

16. How would you activate all of the scripts in the "vuln" category?

```
--script=vuln
```
