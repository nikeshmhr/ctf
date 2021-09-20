# NSE Scripts: Searching for Scripts

## Notes

[Website](https://nmap.org/nsedoc/) contains a list of all offical scripts. Nmap stores its scripts on Linux at `/usr/share/nmap/scripts`.
`cat /usr/share/nmap/scripts/script.db` to search for installed scripts

## Questions

1. Search for "smb" scripts in the `/usr/share/nmap/scripts/` directory using either of the demonstrated methods. What is the filename of the script which determines the underlying OS of the SMB server?

```
smb-os-discovery.nse
```

2. Read through this script. What does it depend on?

```
smb-brute
```
