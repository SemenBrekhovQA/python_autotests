import requests

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = 'aa78fd6cfae09110eb164337686bbf1a'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : 'aa78fd6cfae09110eb164337686bbf1a'}
body_сreation =  {
    "name": "ТестПупсан",
    "photo_id": 37
}

creation = requests.post(url = f'{URL}pokemons', headers = HEADER, json = body_сreation)
print(creation.text)

created_pokemon = creation.json()['id']
print(created_pokemon)


body_rename =  {
    "pokemon_id": created_pokemon,
    "name": "ТестПупсик",
    "photo_id": 37
}
rename = requests.put(url = f'{URL}pokemons', headers = HEADER, json = body_rename)
print(rename.text)


body_catch =  {
    "pokemon_id": created_pokemon
}
catch = requests.post(url = f'{URL}trainers/add_pokeball', headers = HEADER, json = body_catch)
print(catch.text)

'''body_knockout = {
    "pokemon_id": "39206"
}
knockout = requests.post(url = f'{URL}pokemons/knockout', headers = HEADER, json = body_knockout)

print(knockout.text)'''