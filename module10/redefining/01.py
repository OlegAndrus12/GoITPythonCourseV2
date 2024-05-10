class Adder:
    def __add__(self, obj):
        raise NotImplemented


class ListAdder(Adder):
    def __init__(self, value):
        self.value = value

    def __add__(self, obj):
        return self.value + obj.value


class DictAdder(Adder):
    def __init__(self, value):
        self.value = value

    def __add__(self, obj):
        return {**self.value, **obj.value}


la1 = ListAdder([1, 2])
la2 = ListAdder([3, 4])

print(la1 + la2)

da1 = DictAdder({"Volodymyr": 10, "Sergiy": 12})
da2 = DictAdder({"Roman": 10, "Katia": 7})

print(da1 + da2)
