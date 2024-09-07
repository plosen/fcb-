from random import randint
import requests

class Pokemon:
    pokemons = {}

    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = randint(1, 1000)

        # Новые свойства
        self.name = self.get_name()
        self.img = self.get_img()
        self.types = self.get_types()
        self.abilities = self.get_abilities()
        self.stats = self.get_stats()

        Pokemon.pokemons[pokemon_trainer] = self

    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['forms'][0]['name']
        else:
            return "Pikachu"

    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['sprites']['front_default']
        else:
            return "https://via.placeholder.com/150?text=No+Image"

    def get_types(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            types = [t['type']['name'] for t in data['types']]
            return types
        else:
            return ["Unknown"]

    def get_abilities(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            abilities = [a['ability']['name'] for a in data['abilities']]
            return abilities
        else:
            return ["Unknown"]

    def get_stats(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
            return stats
        else:
            return {"hp": 0, "attack": 0, "defense": 0}

    def update_name(self, new_name):
        self.name = new_name

    def update_img(self, new_img_url):
        self.img = new_img_url

    def info(self):
        types = ", ".join(self.types)
        abilities = ", ".join(self.abilities)
        stats = "\n".join([f"{key}: {value}" for key, value in self.stats.items()])

        return (f"Имя: {self.name}\n"
                f"Типы: {types}\n"
                f"Способности: {abilities}\n"
                f"Статистика:\n{stats}")

    def show_img(self):
        return self.img
