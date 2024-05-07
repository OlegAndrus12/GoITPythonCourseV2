#  explain abstraction


class Animal:
    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age

    def get_info(self):
        return f"It's animal. His name is {self.nickname} and he's {self.age} years old"


animal = Animal("Simon", 4)
print(animal.nickname)
animal.age = 5
print(animal.get_info())
