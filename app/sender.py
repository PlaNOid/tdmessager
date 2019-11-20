import requests

username = ''
password = ''

while not username or not password:
    username = input('Enter username: ')
    password = input('Enter password: ')

while True:
    text = input('Enter a message: ')

    r = requests.post(
        'http://127.0.0.1:5000/send/',
        json={'username': username, 'password': password, 'text': text}
    )

    if r.status_code == 200:
        print('Message send')
        print('-' * 10)


