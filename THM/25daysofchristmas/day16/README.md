# File Confusion

```
Need to fix some files.
Use a (python) script to do the following:

extract all the files in the archives
extract metadata from the files
extract text from the files
```

## Notes

```

```

## Questions

1. How many files did you extract(excluding all the .zip files)

```
use ziplib to extract upto 2 levels
50
```

2. How many files contain Version: 1.1 in their metadata?

```
install exiftool
install python wrapper pyexiftool
extract meta look for XMP:Version where value is 1.1

3
```

3. Which file contains the password?

```
read each file and search for word password
dL6w.txt
```
