import random


set_of_letters = ["A", "B", "C", "E", "H", "I", "K", "M", "O", "P", "T", "X"]
set_of_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

l1 = random.choices(set_of_letters, k=2)
l2 = random.choices(set_of_letters, k=2)
l3 = random.choices(set_of_numbers, k=4)
res = l1 + l3 + l2

print(l1)
print(l2)
print(l3)
print(res)
number = "".join(l1 + [" "] + l3 + [" "] + l2)


print(number)


import random

start = "AI"
set_of_letters = ["A", "B", "C", "E", "H", "I", "K", "M", "O", "P", "T", "X"]
set_of_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

numbers = "".join(random.choices(set_of_numbers, k=4))
print(random.choices(set_of_numbers, k=4))
last_l = "".join(random.choices(set_of_letters, k=2))

print(f"{start} {numbers} {last_l}")
