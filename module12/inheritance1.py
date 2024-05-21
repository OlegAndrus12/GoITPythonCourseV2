# simple inheritance example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person : {self.name} is {self.age} years old"

class PythonDeveloper(Person):
    def __init__(self, name, age, liters_of_coffee, years_of_experience):
        # Person.__init__(self, name, age)
        super().__init__(name, age)
        self.liters_of_coffee = liters_of_coffee
        self.years_of_experience = years_of_experience

    def __str__(self):
        base_info = super().__str__()
        return base_info + f" I finished {self.liters_of_coffee} over the last {self.years_of_experience} years"


dev = PythonDeveloper("John Doe", 29, 102, 5)
print(dev)
print(issubclass(PythonDeveloper, Person))