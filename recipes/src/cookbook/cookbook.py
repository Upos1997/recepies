from dataclasses import dataclass

from recipes.src.cookbook.recipe import Recipe
import json


@dataclass
class CookBook:
    def __init__(self):
        self.recipes: list[Recipe] = []
        self.ingredients: dict[str, list[Recipe]] = {}
        self.tags: dict[str, list[Recipe]] = {}
        self.sources: dict[str, list[Recipe]] = {}

    def add_recipe(self, recipe: Recipe) -> None:
        def update_dict(adict: dict[str, list[Recipe]], item: str) -> None:
            if item in adict:
                adict[item].append(recipe)
            else:
                adict[item] = [recipe]

        self.recipes.append(recipe)
        for ingredient_name in recipe.ingredients.keys():
            update_dict(self.ingredients, ingredient_name)
        for tag in recipe.tags:
            update_dict(self.tags, tag)
        update_dict(self.sources, recipe.source)

    def delete_recipe(self, recipe: Recipe) -> None:
        for ingredient in recipe.ingredients.keys():
            self.ingredients[ingredient].remove(recipe)
        self.recipes.remove(recipe)

    @staticmethod
    def __filter_by_name(name: str, intermediate_solution: list[Recipe]) -> list[Recipe]:
        return [recipe for recipe in intermediate_solution if recipe.name == name]

    @staticmethod
    def __filter_by_ingredient(ingredient: str, intermediate_solution: list[Recipe]) -> list[Recipe]:
        return [recipe for recipe in intermediate_solution if recipe.contains(ingredient)]

    @staticmethod
    def __filter_by_tag(tag: str, intermediate_solution: list[Recipe]) -> list[Recipe]:
        return [recipe for recipe in intermediate_solution if tag in recipe.tags]

    @staticmethod
    def __filter_by_source(source: str, intermediate_solution: list[Recipe]) -> list[Recipe]:
        return [recipe for recipe in intermediate_solution if source in recipe.source]

    def __find_recipe_by_name(self, name: str) -> list[Recipe]:
        return list(self.__filter_by_name(name, self.recipes))

    def __find_recipe_by_ingredient(self, ingredient: str) -> list[Recipe]:
        return self.ingredients[ingredient]

    def __find_recipe_by_tag(self, tag: str) -> list[Recipe]:
        return self.tags[tag]

    def __find_recipe_by_source(self, source: str) -> list[Recipe]:
        return self.sources[source]

    def find_recipes(self, names: list[str], ingredients: list[str],
                     tags: list[str], sources: list[str]) -> list[Recipe]:
        short_list = []
        if ingredients:
            short_list = self.__find_recipe_by_ingredient(ingredients[0])
            del ingredients[0]
        elif tags:
            short_list = self.__find_recipe_by_tag(tags[0])
            del tags[0]
        elif sources:
            short_list = self.__find_recipe_by_source(sources[0])
            del sources[0]
        elif names:
            short_list = self.__find_recipe_by_name(names[0])
            del names[0]
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
        return {"recipes": [recipe.serialize() for recipe in self.recipes]}

    @staticmethod
    def __deserialize(serialized_cookbook):
        result = CookBook()
        for serialized_recipe in serialized_cookbook["recipes"]:
            result.add_recipe(Recipe.deserialize(serialized_recipe))
        return result

    def save(self, address: str) -> None:
        with open(address, "w") as file:
            json.dump(self.__serialize(), file)

    @staticmethod
    def load(address: str):
        with open(address, "r") as file:
            return CookBook.__deserialize(json.load(file))
