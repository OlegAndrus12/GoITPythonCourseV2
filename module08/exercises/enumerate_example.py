languages = ["Python", "Java", "JavaScript"]

# enumerate the list
enumerated_languages = enumerate(languages, start=0)

# convert enumerate object to list
print(list(enumerated_languages))


for position, element in enumerate(languages):
    print(position, element)
