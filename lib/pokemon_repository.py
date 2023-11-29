from lib.pokemon import *

class PokemonRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM pokemons')
        
        pokemons = []

        for row in rows:
            pokemon = Pokemon(row['id'], row['name'], row['power_type'])
            pokemons.append(pokemon)
        return pokemons