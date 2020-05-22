#!/usr/bin/env python3
import requests
import json

host = 'http://10.10.169.100'
port = '3000'

next = ['']
flag = ''

while True:
    index = len(next) - 1
    print(flag)

    response = requests.get(host + ':' + port + '/' + next[index])
    response_json = json.loads(response.text)
    print(response.json())
    if(response_json["value"] != "end" and response_json["next"] != "end"):
        next.append(response_json["next"])
        flag = flag + response_json["value"]
    else:
        break

print(flag)