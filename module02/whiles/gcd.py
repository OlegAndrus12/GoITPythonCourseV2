first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))


# НСД


gcd = min(first, second)  # 4

while not (first % gcd == 0 and second % gcd == 0):
    gcd -= 1

print(gcd)
