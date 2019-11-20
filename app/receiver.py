import requests
import time
from datetime import datetime


last_received = 0

while True:
    r = requests.get(
        'http://127.0.0.1:5000/messages/',
        params={'after': last_received}
    )

    if r.status_code == 200:
        m = r.json()['messages']
        for me in m:
            print(datetime.fromtimestamp(me['time']))
            print('From: ', me['username'])
            print(me['text'])
            print('=' * 20)
            last_received = me['time']

    time.sleep(1)
