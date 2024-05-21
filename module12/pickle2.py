import pickle


class User:
    # Custom class with all class variables given in the __init__()
    def __init__(self, name, age, active, balance, friends):
        self.name = name
        self.age = age
        self.active = active
        self.balance = balance
        self.friends = friends

    def __getstate__(self):
        print("ASdasd")
        state = self.__dict__.copy()
        return state

    def __setstate__(self, state):
        print("ASdsadsadsadsdsa")


user = User(name="John", age=28, friends=["Jane", "Tom"], balance=20.70, active=True)
print(user.__dict__)
a = pickle.dumps(user)
print(a)
pickle.loads(a)