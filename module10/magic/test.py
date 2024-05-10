# https://peps.python.org/pep-0008/#method-names-and-instance-variables


class P:
    def __init__(self, x):
        self.__x = x


class C(P):
    def __init__(self, x):
        super().__init__(x)


p = C(2)


class Person:
    def __init__(self, name):
        self.__name = None
        self.name = name

    @property
    def name2(self):
        return self.__name

    @name2.setter
    def name(self, name):
        print("here")
        if (type(name) == str) and (len(name) > 0):
            self.__name = name


person = Person(123)
print(person.name)  # None
