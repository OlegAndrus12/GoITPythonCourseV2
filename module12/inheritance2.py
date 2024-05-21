# simple inheritance example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):\
        return f"Person : {self.name} is {self.age} years old"

class PythonDeveloper(Person):
    def __init__(self, liters_of_coffee=0, years_of_experience=0, **kwargs):
        # 1st way
        # super().__init__(**kwargs)
        # 2nd way
        #
        self.liters_of_coffee = liters_of_coffee
        self.years_of_experience = years_of_experience

    def __str__(self):
        base_info = super().__str__()
        return base_info + f" I finished {self.liters_of_coffee} litters of coffe over the last {self.years_of_experience} years"


class FrontendDeveloper(Person):
    def __init__(self, most_liked_framework, **kwargs):
        # 1st way
        # super().__init__(**kwargs)
        # 2nd way
        #
        self.most_liked_framework = most_liked_framework

    def __str__(self):
        base_info = super().__str__()
        return base_info + f" I'm a huge fan of {self.most_liked_framework}"


class FullstackDeveloper(FrontendDeveloper, PythonDeveloper):
    def __init__(self, company_name, **kwargs):
        self.company_name = company_name
        # 1st way
        # super().__init__(**kwargs)
        # 2nd way
        Person.__init__(self, name=kwargs.get("name"), age=kwargs.get("age"))
        FrontendDeveloper.__init__(self, most_liked_framework=kwargs.get("most_liked_framework"))
        PythonDeveloper.__init__(self, liters_of_coffee=kwargs.get("liters_of_coffee"), years_of_experience=kwargs.get("years_of_experience"))

fullstack = FullstackDeveloper("Levi9", most_liked_framework="ReactJS", name="Oleh", age=24)
print(fullstack)