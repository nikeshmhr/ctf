import zipfile
import os
import exiftool
import base64

dir1 = 'extracted-level1'
dir2 = 'extracted-level2'

# Level 1 extract
with zipfile.ZipFile('final-final-compressed.zip', 'r') as zipRef:
    zipRef.extractall(dir1)

# Level 2 extract
for dir in os.listdir(dir1):
    location = dir1 + os.sep + dir
    with zipfile.ZipFile(location, 'r') as zipRef:
        zipRef.extractall(dir2)
files = os.listdir(dir2)
print("No. of files: %s" % len(files))

# Q.2: Looking metadata to find info.
# NEEDS TO CLONE git clone git://github.com/smarnach/pyexiftool.git
files = os.listdir(dir2)
count = 0
with exiftool.ExifTool() as et:
    for file in files:
        metadata = et.get_metadata(dir2 + os.sep + file)
        if (metadata.get("XMP:Version") == 1.1):
            count += 1
print("No. of file with Version (1.1): %s" % count)

## Q.3: Reading file for password
files = os.listdir(dir2)
for file in files:
    location = dir2 + os.sep + file
    try:
        with open(location, 'r') as reader:
            content = reader.read()
            if("password" in content):
                print(file)
    except:
        continue

# Cleanup
os.system('rm -rf ' + dir1)
os.system('rm -rf ' + dir2)