import random


coin = {1: "Орел", 2: "Решка"}

count_O = 0
count_P = 0
sequence = list()

while count_O < 4 and count_P < 4:
    choice = random.randint(1, 2)
    if choice == 1:
        count_O += 1
        count_P = 0
    else:
        count_P += 1
        count_O = 0
    name = coin[choice]
    sequence.append(name)

print(sequence)
print(len(sequence))
