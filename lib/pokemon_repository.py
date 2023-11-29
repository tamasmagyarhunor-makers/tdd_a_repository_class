from lib.pokemon import *

class PokemonRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        pass