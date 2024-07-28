import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = 'aa78fd6cfae09110eb164337686bbf1a'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : 'aa78fd6cfae09110eb164337686bbf1a'}
TRAINER_ID = '5602'

def test_status_code():
    response = requests.get(url = f'{URL}trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_trainer_name():
    response_get = requests.get(url = f'{URL}trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Oksik'


    '{"status":"success","data":[{"id":"5602","trainer_name":"Oksik","level":"2","pokemons":["39207","45582","45542","45515","45506","45578","45541","45579","45580","44524","44523","44522","45511","39208","45513","45529","45517","45518","45512","45514","45522","45516","45543","45525","45574","45510","45519","45507","45530","45523","45572","45575","45521","39206"],"pokemons_alive":["45578","45579"],"pokemons_in_pokeballs":[],"get_history_battle":"0","is_premium":false,"premium_duration":0,"avatar_id":2,"city":"Golotsino"}]}'