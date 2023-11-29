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
    
    def find(self, pokemon_id):
        rows = self._connection.execute('SELECT * FROM pokemons WHERE id = %s', [pokemon_id])
        pokemon = Pokemon(rows[0]['id'], rows[0]['name'], rows[0]['power_type'])
        
        return pokemon
    