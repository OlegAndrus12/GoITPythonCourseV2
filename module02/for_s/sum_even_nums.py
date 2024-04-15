even_nums = [1, 2, 3, 4, 65, 653, 32]
total = 0

for x in even_nums:
    if x % 2 != 0:
        break
    total += x
else:
    print("For loop executed normally")
    print(f"Sum of numbers {total}")
