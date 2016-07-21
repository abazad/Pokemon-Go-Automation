import json

def list():
    global pokemonList
    pokemonList=json.load(open('pokemon.json'))