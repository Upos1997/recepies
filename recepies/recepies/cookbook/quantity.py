from dataclasses import dataclass


@dataclass
class Quantity:
    def __init__(self, amount: float = 4, metric: str = "people"):
        self.amount: float = amount
        self.metric: str = metric

    def __repr__(self) -> str:
        return f"Quantity({self.amount}, {self.metric})"

    def print(self, multiplier: float = 1):
        return f"{self.amount * multiplier} {self.metric}"

    def get_multiplier(self, quantity):
        if quantity.metric == self.metric:
            return self.amount / quantity.amount
        raise ValueError()

    def serialize(self):
        return (self.amount, self.metric)

    @staticmethod
    def deserialize(serialized_quantity):
        return Quantity(serialized_quantity[0], serialized_quantity[1])
