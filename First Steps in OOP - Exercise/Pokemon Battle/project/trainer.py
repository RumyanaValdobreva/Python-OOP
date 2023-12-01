# from typing import List
from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        # self.pokemons: List[Pokemon] = []
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        # if pokemon.name in [p.name for p in self.pokemons]:
        for p in self.pokemons:
            if p.name == pokemon.name:
                return "This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        for pokemon_object in self.pokemons:
            if pokemon_object.name == pokemon_name:
                self.pokemons.remove(pokemon_object)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        output_data = [f"Pokemon Trainer {self.name}", f"Pokemon count {len(self.pokemons)}"]
        for p in self.pokemons:
            output_data.append(f"- {p.pokemon_details()}")
        return "\n".join(output_data)
