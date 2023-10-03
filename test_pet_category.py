import pytest
import requests
import configparser

config = configparser.ConfigParser()
config.read('configuration.ini')

user = config['creds']['username']
password = config['creds']['password']
url = config['uri']['url']
endpoint = '/api/category/'


@pytest.fixture
def session():
    session = requests.Session()
    session.auth = (user, password)
    yield session


@pytest.fixture
def response(session):
    yield session.get(f'{url}{endpoint}?limit=15&offset=0')
    session.close()


def test_pet_category_should_return_status_200(response):
    assert response.status_code == 200


def test_pet_category_pagination_check(response):
    count = response.json().get('count')
    results_size = len(response.json().get('results'))
    assert results_size == count or results_size == 15


def test_pet_category_should_return_category_by_id(response, session):
    id = response.json().get('results')[0].get('id')
    new_response = session.get(f'{url}{endpoint}{id}')
    assert new_response.status_code == 200
    assert new_response.json().get('id') == id
