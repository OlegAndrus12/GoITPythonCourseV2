from __future__ import annotations

import pickle

# show load without class
class Car:
    store_name = "Autoria"

    def __init__(self, year, mark, model, color, price):
        self.year = year
        self.mark = mark
        self.model = model
        self.color = color
        self.price = price

    def __str__(self):
        return f"{self.store_name} - {self.mark}.{self.model}: {self.year}, {self.color}, '{self.price}'"


c = Car(2023, "Ford", "Fusion", "red", 12000)

serialized_car = pickle.dumps(c)
print(serialized_car)
deserialized_car = pickle.loads(serialized_car)
print(deserialized_car)
print(c == deserialized_car)
