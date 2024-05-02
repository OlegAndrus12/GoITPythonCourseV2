first_names = ["Ivan", "Nick", "John"]
last_names = ["Walker", "Doe", "Crawn"]
grades = [77, 83, 90]


print(list(zip(first_names, last_names, grades)))

last_names.pop()
print(list(zip(first_names, last_names, grades)))
