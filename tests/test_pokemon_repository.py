from lib.pokemon_repository import *

def test_pokemon_repository_all(db_connection):
    db_connection.seed('tests/seeds_pokemon.sql')
    repository = PokemonRepository(db_connection)

    pokemons = repository.all()

    assert len(pokemons) == 2
    assert pokemons == [
        Pokemon(1, "Pikachu", "electric"),
        Pokemon(2, "Bulbasaur", "grass/poison")
    ]

def test_pokemon_repositoru_find(db_connection):
    db_connection.seed('tests/seeds_pokemon.sql')
    repository = PokemonRepository(db_connection)
    
    pokemon = repository.find(2)

    assert pokemon == Pokemon(2, 'Bulbasaur', 'grass/poison')
