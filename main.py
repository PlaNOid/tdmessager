import datetime
import time
from flask import Flask, request

app = Flask(__name__)

messages = [
    {
        'username': 'John',
        'time': time.time(),
        'text': 'Hello!'
    },
    {
        'username': 'Mary',
        'time': time.time(),
        'text': 'Hello John!'
    }
]

users = {
    'John': '12345',
    'Mary': '12345',
    'admin': 'root!',
}


@app.route("/")
def main():
    return 'Welcome to messenger Main Page'


@app.route("/status/")
def status():
    date = datetime.datetime.now()
    str_from_date = datetime.datetime.strftime
    return {
        'status': True,
        'date': str_from_date(date, '%Y-%m-%d'),
        'time': str_from_date(date, '%H:%M:%S'),
        'total_messages_send': len(messages),
        'total_users_registered': len(users),
    }


@app.route("/send/", methods=['POST'])
def send_method():
    """
    JSON {"username": str, "text": str}
    username, text - not none
    :return: {"ok": bool}
    """
    username = request.json['username']
    password = request.json['password']

    text = request.json['text']

    # user registartion

    if username not in users:
        users[username] = password

    # validate data
    if not isinstance(username, str) or len(username) == 0:
        return {'ok': False}

    if not isinstance(text, str) or len(text) == 0:
        return {'ok': False}

    if users[username] != password:
        return {'ok': False}

    messages.append({'username': username, 'time': time.time(), 'text': text})

    return {'ok': True}


@app.route("/messages/")
def messages_method():
    """
    Param after - float, отметка веремени после котрой будут сообщения
    :return: {
                "messages": [
                    {
                        "username": str,
                        "time": float,
                        "text": str
                    },
                ]
            }
    """
    after = float(request.args['after'])
    filtered_messages = [message for message in messages if message['time'] > after]
    return {'messages': filtered_messages}


app.run()
