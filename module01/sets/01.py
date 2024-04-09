l1 = set(["Red", "Green", "Black", "White"])
l2 = set(["Red", "White", "Purple"])

# res = l1.intersection(l2)
# | = pipe
#  & - перетин, | об'єднання, ^ симетрична різниця, - різниця

# always return a copy

print(l1.union(l2))
print(l1 | l2)

print(l1.intersection(l2))
print(l1 & l2)

print(l1.difference(l2))
print(l1 - l2)

print(l1.symmetric_difference(l2))
print(l1 ^ l2)

l1.isdisjoint(l2)  # Determines whether or not two sets have any elements in common


print(l2.issubset(l1))
