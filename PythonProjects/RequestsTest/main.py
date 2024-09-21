import requests

# Подсказка {'id': '7721', 'trainer_token': '0690dec79c8aa90a7d977a302af2e092', 'trainer_name': 'Shortdeath'}

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '0690dec79c8aa90a7d977a302af2e092'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "generate",
    "photo_id": -1
}

body_change_name = {
    "pokemon_id": "73354",
    "name": "PYTHON",
    "photo_id": 2
}

body_pokeball = {
    "pokemon_id": "73354"
}

# response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
# print(response_create.text)

# response_change_name =  requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
# print(response_change_name.text)

response_pokeball =  requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)