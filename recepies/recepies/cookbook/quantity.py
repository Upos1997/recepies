from dataclasses import dataclass


@dataclass
class Quantity:
    def __init__(self, amount: float = 4, metric: str = "people"):
        self.amount: float = amount
        self.metric: str = metric

    def __repr__(self) -> str:
        return f"Quantity({self.amount}, {self.metric})"

    def print(self, multiplier: float = 1) -> None:
        return f"{self.amount * multiplier} {self.metric}"

    def get_multiplier(self, quantity) -> float:
        if quantity.metric == self.metric:
            return self.amount / quantity.amount
        else:
            raise ValueError()

    def serialize(self) -> dict:
        return {"amount": self.amount, "metric": self.metric}

    @staticmethod
    def deserialize(serialized_quantity):
        return Quantity(serialized_quantity["amount"], serialized_quantity["metric"])
