with open('wordlist.txt', 'w') as file:
    for i in range(1, 10000):
        file.write(f'{i:04}\n')