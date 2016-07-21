import json

def list():
    global pokemon_list
    pokemon_list=json.load(open('pokemon.json'))