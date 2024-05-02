import collections

Point = collections.namedtuple("Point", ["x", "y", "z"])
p = Point(1, 2, 3)
print(p.x, p.y, p.z)

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])
print(Cat.__name__)
cat = Cat("Simon", 4, "Krabat")
print(type(cat))
print(f"This is a cat {cat.nickname}, {cat.age} age, his owner {cat.owner}")
