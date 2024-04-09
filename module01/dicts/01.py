# count values
# git add 01.py
# git commit -m "dict example"
# git push

data = {
    2000: "Ford",
    2001: "Toyota",
    2002: "Jeep",
    2003: "Jeep",
    2004: "Ford",
    2005: "Ford",
    2006: "Honda",
    2007: "Hyndai",
    2007: "Hyndai",
    2008: "Ford",
}
# iterate dicts:
for key in data:
    print(key, ":", data[key])

for key,value in data.items():
    print(key, ":", value)
# return a list of years where Fords were sold out
choice = "Ford"
res = list()
for year in data:
    if choice == data[year]:
        res.append(year)

print(res)


# extend data with new records

new_data = {2008: "Linkoln", 2009: "Land Rover"}
data.update(new_data)
print(data)

# safe get

data.get(2024, None)

print(data)
# clear dict

data.clear()
print(data)

# popitem -> last key-value pair, pop -> by specific key
