from dataclasses import dataclass
from recepies.cookbook.recepy import Recepy
import json


@dataclass
class CookBook:
    def __init__(self):
        self.recepies = []
        self.ingredients = {}
        self.tags = {}

    def add_recepy(self, recepy: Recepy) -> None:
        def update_dict(dict: dict, item) -> None:
            if item in dict:
                dict[item].append(recepy)
            else:
                dict[item] = [recepy]

        self.recepies.append(recepy)
        for ingredient in recepy.ingredients.keys():
            update_dict(self.ingredients, ingredient)
        for tag in recepy.tags:
            update_dict(self.tags, tag)

    def delete_recepy(self, recepy: Recepy) -> None:
        for ingredient in recepy.ingredients.keys():
            self.ingredients[ingredient].remove(recepy)
        self.recepies.remove(recepy)

    def filter_by_name(name: str, list: list[Recepy]) -> list[Recepy]:
        return [recepy for recepy in list if name in recepy.name]

    def filter_by_ingredient(ingredient: str, list: list[Recepy]) -> list[Recepy]:
        return list(filter(lambda recepy: recepy.contains(ingredient)), list)

    def filter_by_tag(tag: str, list: list[Recepy]) -> list[Recepy]:
        return list(filter(lambda recepy: tag in recepy.tags), list)

    def find_recepy_by_name(self, name: str) -> list[Recepy]:
        return self.filter_by_name(name, self.recepies)

    def find_recepy_by_ingredient(self, ingredient: str) -> list[Recepy]:
        return self.ingredients[ingredient]

    def find_recepy_by_tag(self, tag: str) -> list[Recepy]:
        return self.tags[tag]

    def save(self, address: str):
        with open(address, "w") as file:
            json.dump([recepy.serialize() for recepy in self.recepies], file)

    def load(self, file):
        self.recepies = []
        self.ingredients = {}
        self.tags = {}
        for recepy in json.load(file):
            self.add_recepy(Recepy.deserialize(recepy))
        file.close()

    def load_str(self, address: str):
        with open(address, "r") as file:
            self.load(file)
