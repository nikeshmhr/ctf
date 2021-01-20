# [Section 5: Advanced File Operations] ln

## Notes
ln is a weird one, because it has two different main uses. One of those is what's known as "hard linking", which completely duplicates the file, and links the duplicate to the original copy. Meaning What ever is done to the created link, is also done to the original file. The ln syntax is `ln source destination.`

The next form of linking is symbolic linking(symlink). While a hard linked file contains the data in the original file, a symbolic link is just a glorified reference. Meaning that the actual symbolic link has no data in it at all, it's just a reference to another file. 

The syntax for a symbolic link is the exact same, but it uses the -s flag, so to create a symbolic link, you would run `ln -s <file> <destination>`.

ls even shows that its a symbolic link with the arrow pointing to what the link is referencing. It is important to note the permissions on the symlink. It has full 777 perms meaning that in theory you can execute the symlink, however since it is just a reference, in reality it has the same perms as the original file.


## Questions
1. How would I link /home/test/testfile to /tmp/test
```
ln /home/test/testfile /tmp/test
```