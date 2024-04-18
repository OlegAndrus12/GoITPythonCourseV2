import random

amount = 4

array = [1, 2, 4, 2, 122, 13]
array_sorted = sorted(array)

print(array)
print("******")
attempt = 0


while array_sorted != array:
    attempt += 1
    random.shuffle(array)
    print(f"# {attempt}, arr: {array}")
