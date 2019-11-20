import requests

host = 'http://127.0.0.1:5000'

def test_main_method():
    resp = requests.get(host)
    assert resp.status_code == 200


def test_status_method():
    resp = requests.get(f'{host}/status/')
    assert resp
    assert resp.status_code == 200
    response_json = resp.json()
    assert 'status' in response_json
    assert response_json['status']
    assert 'date' in response_json
    assert 'time' in response_json
    assert 'total_messages_send' in response_json
    assert 'total_users_registered' in response_json


def test_send_method():
    resp = requests.post(
        f'{host}/send/',
        json={
            'username': 'test_user',
            'password': 'test',
            'text': 'test Message text',
        }
    )
    assert resp
    assert resp.status_code == 200
    assert resp.json()['ok']

    resp = requests.post(
        f'{host}/send/',
        json={
            'username': 'test_user',
            'password': 'wrong password',
            'text': 'test Message text',
        }
    )
    assert resp
    assert resp.status_code == 200
    assert not resp.json()['ok']

    resp = requests.post(
        f'{host}/send/',
        json={
            'username': 'test_user',
            'password': 'test',
            'text': ''
        }
    )
    assert resp
    assert resp.status_code == 200
    assert not resp.json()['ok']

    resp = requests.post(
        f'{host}/send/',
        json={
            'username': 'test_user',
            'password': 'test',
            'text': {'not a': 'string'}
        }
    )
    assert resp
    assert resp.status_code == 200
    assert not resp.json()['ok']

    resp = requests.post(
        f'{host}/send/',
        json={
            'username': 'new_test_user',
            'password': 'new_password',
            'text': 'Message'
        }
    )
    assert resp
    assert resp.status_code == 200
    assert resp.json()['ok']


test_main_method()
test_status_method()
test_send_method()

print('All test is passed')
