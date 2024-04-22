
cars = {
        "Ford" : 2005,
        "Mitsubishi" : 2000,
        "BMW" : 2019,
        "VW" : 2005,
        }
# return a message with a list of cars sorted by name

names = list(cars.keys())
names.sort()
print(" | ".join(names))

