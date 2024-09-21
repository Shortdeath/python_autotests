import requests
import pytest

# {'id': '7721', 'trainer_token': '0690dec79c8aa90a7d977a302af2e092', 'trainer_name': 'Shortdeath'}

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '0690dec79c8aa90a7d977a302af2e092'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '7721'

def test_status_code ():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response ():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["id"] == TRAINER_ID