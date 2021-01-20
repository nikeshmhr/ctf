# [Section 6: Miscellaneous]: Adding users and groups

## Notes
You know about how to modify permissions for users and groups, therefore it's helpful to know how to create them. Luckily Linux provides a nice helpful way to do this, with `adduser` and `addgroup`. The syntax for both of these commands are `adduser username` and `addgroup groupname`.

It's important to note that only root has permissions to add users and groups, as seen with the failure when I attempted to run the commands without sudo. You may be wondering how to add a user to a group. that is done with the `usermod` command, the syntax for that is `usermod -a -G <groups seperated by commas> <user>`. Meaning if I wanted to add the user `noot` to `b` I would run `usermod -a -G b noot`.

## Question
1. How would I add the user test to the group test
```
sudo usermod -a -G test test
```