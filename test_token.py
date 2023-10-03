import configparser
import requests


config = configparser.ConfigParser()
config.read('configuration.ini')

user = config['creds']['username']
password = config['creds']['password']
url = config['uri']['url']


def test_token_should_return_status_code_200():
    session = requests.Session()
    session.auth = (user, password)
    body = {'username': 'yana', 'password': '1111'}
    response = session.post(url + '/api/token/auth/', body)
    assert response.status_code == 200


def test_token_should_have_right_json():
    session = requests.Session()
    session.auth = (user, password)
    body = {'username': 'yana', 'password': '1111'}
    response = session.post(url + '/api/token/auth/', body)
    assert 'token' in response.json().keys() and isinstance(response.json().keys(), str)


