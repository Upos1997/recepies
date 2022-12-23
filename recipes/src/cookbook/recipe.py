from dataclasses import dataclass
import os
from recipes.src.cookbook.quantity import Quantity


@dataclass
class Recipe:
    def __init__(
            self,
            name: str = "Empty",
            ingredients=None,
            instructions: str = "Nothing",
            tags=None,
            source: str = "",
            image=None,
            quantity: Quantity = Quantity(),
            notes: str = "",
    ):
        if ingredients is None:
            ingredients = {}
        if tags is None:
            tags = []
        self.name: str = name
        self.ingredients: dict[str, Quantity] = ingredients
        self.instructions: list[str] = instructions.split("|")
        self.tags: list[str] = tags
        self.source: str = source
        self.image = image
        self.quantity: Quantity = quantity
        self.notes: str = notes

    def __repr__(self) -> str:
        return f"Recipe({self.name})"

    def contains(self, search_ingredient: str) -> list[str]:
        return [
            ingredient
            for ingredient in self.ingredients.keys()
            if search_ingredient in ingredient
        ]

    def print(self, quantity: Quantity = None) -> None:
        if quantity is None:
            multiplier: float = 1
        else:
            multiplier = quantity.get_multiplier(self.quantity)
        print(
            f"""{self.name}
INGREDIENTS
-----------
{os.linesep.join([f"{quantity.print(multiplier)} {ingredient}" for ingredient, quantity in self.ingredients.items()])}
-----------
{"".join(
                [
                    str(part * multiplier) if isinstance(part, float) else part
                    for part in self.instructions
                ]
            )}
-----------
{self.notes}"""
        )

    def serialize(self) -> dict:
        return {
            "name": self.name,
            "ingredients": [{"name": ingredient, "quantity": quantity.serialize} for ingredient, quantity in
                            self.ingredients.items()],
            "instructions": "".join(self.instructions),
            "tags": self.tags,
            "source": self.source,
            "image": self.image,
            "quantity": self.quantity.serialize(),
            "notes": self.notes,
        }

    @staticmethod
    def deserialize(serialized_recipe):
        name = serialized_recipe["name"]
        ingredients = {
            ingredient["name"]: Quantity.deserialize(ingredient["quantity"])
            for ingredient in serialized_recipe["ingredients"]
        }
        instructions = serialized_recipe["instructions"]
        tags = serialized_recipe["tags"]
        source = serialized_recipe["source"]
        image = serialized_recipe["image"]
        quantity = Quantity.deserialize(serialized_recipe["quantity"])
        notes = serialized_recipe["notes"]
        return Recipe(name, ingredients, instructions, tags, source, image, quantity, notes)
