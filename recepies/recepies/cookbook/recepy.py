from dataclasses import dataclass
import os
from recepies.cookbook.quantity import Quantity


@dataclass
class Recepy:
    def __init__(
        self,
        name: str,
        ingredients: dict,
        instructions: str,
        tags: list[str] = "",
        image=None,
        quantity: Quantity = Quantity(),
        notes: str = "",
    ):
        self.name: str = name
        self.ingredients: dict = ingredients
        self.instructions: list = instructions.split("|")
        self.tags: list = tags
        self.image = image
        self.quantity: Quantity = quantity
        self.notes: str = notes

    def __repr__(self) -> str:
        return f"Recepy({self.name})"

    def contains(self, search_ingredient: str) -> list:
        return [
            ingredient
            for ingredient in self.ingredients.values()
            if search_ingredient in ingredient
        ]

    def print(self, quantity="") -> None:
        if quantity == "":
            multiplier = 1
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

    def serialize(self):
        return [
            self.name,
            [
                (quantity.serialize(), ingredient)
                for ingredient, quantity in self.ingredients.items()
            ],
            "".join(self.instructions),
            self.tags,
            self.image,
            self.quantity.serialize(),
            self.notes,
        ]

    @staticmethod
    def deserialize(serialized_list):
        name = serialized_list[0]
        ingredients = {
            ingredient[1]: Quantity.deserialize(ingredient[0])
            for ingredient in serialized_list[1]
        }
        instructions = serialized_list[2]
        tags = serialized_list[3]
        image = serialized_list[4]
        quantity = Quantity.deserialize(serialized_list[5])
        notes = serialized_list[6]
        return Recepy(name, ingredients, instructions, tags, image, quantity, notes)
