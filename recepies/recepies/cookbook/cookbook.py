from dataclasses import dataclass
from recepies.cookbook.recepy import Recepy
import json


@dataclass
class CookBook:
    def __init__(self):
        self.recepies: list[Recepy] = []
        self.ingredients: dict[str, list[Recepy]] = {}
        self.tags: dict[str, list[Recepy]] = {}
        self.sources: dict[str, list[Recepy]] = {}

    def add_recepy(self, recepy: Recepy) -> None:
        def update_dict(dict: dict[str, list[Recepy]], item: str) -> None:
            if item in dict:
                dict[item].append(recepy)
            else:
                dict[item] = [recepy]

        self.recepies.append(recepy)
        for ingredient_name in recepy.ingredients.keys():
            update_dict(self.ingredients, ingredient_name)
        for tag in recepy.tags:
            update_dict(self.tags, tag)
        update_dict(self.sources, recepy.source)

    def delete_recepy(self, recepy: Recepy) -> None:
        for ingredient in recepy.ingredients.keys():
            self.ingredients[ingredient].remove(recepy)
        self.recepies.remove(recepy)

    def __filter_by_name(name: str, list: list[Recepy]) -> list[Recepy]:
        return [recepy for recepy in list if recepy.name == name]

    def __filter_by_ingredient(ingredient: str, list: list[Recepy]) -> filter:
        return filter(lambda recepy: recepy.contains(ingredient), list)

    def __filter_by_tag(tag: str, list: list[Recepy]) -> filter:
        return filter(lambda recepy: tag in recepy.tags, list)

    def __filter_by_source(source: str, list: list[Recepy]) -> filter:
        return filter(lambda recepy: source in recepy.source, list)

    def __find_recepy_by_name(self, name: str) -> list[Recepy]:
        return list(self.__filter_by_name(name, self.recepies))

    def __find_recepy_by_ingredient(self, ingredient: str) -> list[Recepy]:
        return self.ingredients[ingredient]

    def __find_recepy_by_tag(self, tag: str) -> list[Recepy]:
        return self.tags[tag]

    def __find_recepy_by_source(self, source: str) -> list[Recepy]:
        return self.sources[source]

    def find_recepies(self, names: list[str], ingredients: list[str], tags: list[str], sources: list[str]) -> list[Recepy]:
        short_list = []
        if (ingredients):
            short_list = self.__find_recepy_by_ingredient(ingredients[0])
            del ingredients[0]
        elif (tags):
            short_list = self.__find_recepy_by_tag(tags[0])
            del tags[0]
        elif (sources):
            short_list = self.__find_recepy_by_source(sources[0])
            del sources[0]
        elif (names):
            short_list = self.__find_recepy_by_name(names[0])
            del names[0]
        short_list = filter(iterable = short_list)
        for name in names:
            short_list = self.__filter_by_name(name, short_list)
        for ingredient in ingredients:
            short_list = self.__filter_by_ingredient(ingredient, short_list)
        for tag in tags:
            short_list = self.__filter_by_tag(tag, short_list)
        for source in sources:
            short_list = self.__filter_by_source(source, short_list)
        return list(short_list)

    def __serialize(self) -> dict:
        return {"recepies": [recepy.serialize() for recepy in self.recepies]}

    @staticmethod
    def __deserialize(serialized_cookbook):
        result = CookBook()
        for serialized_recepy in serialized_cookbook["recepies"]:
            result.add_recepy(Recepy.deserialize(serialized_recepy))
        return result

    def save(self, address: str) -> None:
        with open(address, "w") as file:
            json.dump(self.__serialize(), file)
        
    @staticmethod
    def load(address: str):
        with open(address, "r") as file:
            return CookBook.__deserialize(json.load(file))
