from dataclasses import dataclass
import os
from recepies.cookbook.quantity import Quantity

@dataclass
class Recepy:
    def __init__(
        self,
        name: str,
        ingredients: dict[str, Quantity],
        instructions: str,
        tags: list[str] = "",
        source: str = "",
        image = None,
        quantity: Quantity = Quantity(),
        notes: str = "",
    ):
        self.name: str = name
        self.ingredients: dict[str, Quantity] = ingredients
        self.instructions: list[str] = instructions.split("|")
        self.tags: list[str] = tags
        self.source: str = source
        self.image = image
        self.quantity: Quantity = quantity
        self.notes: str = notes

    def __repr__(self) -> str:
        return f"Recepy({self.name})"

    def contains(self, search_ingredient: str) -> list[str]:
        return [
            ingredient
            for ingredient in self.ingredients.keys()
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

    def serialize(self) -> dict:
        return {
            "name": self.name,
            "ingredients": [{"name": ingredient, "quantity": quantity.serialize} for ingredient, quantity in self.ingredients.items()],
            "instructions": "".join(self.instructions),
            "tags": self.tags,
            "source": self.source,
            "image": self.image,
            "quantitiy": self.quantity.serialize(),
            "notes": self.notes,
        }

    @staticmethod
    def deserialize(serialized_recepy):
        name = serialized_recepy["name"]
        ingredients = {
            ingredient["name"]: Quantity.deserialize(ingredient["quantity"])
            for ingredient in serialized_recepy["ingredients"]
        }
        instructions = serialized_recepy["instructions"]
        tags = serialized_recepy["tags"]
        source = serialized_recepy["source"]
        image = serialized_recepy["image"]
        quantity = Quantity.deserialize(serialized_recepy["quantity"])
        notes = serialized_recepy["notes"]
        return Recepy(name, ingredients, instructions, tags, source, image, quantity, notes)
