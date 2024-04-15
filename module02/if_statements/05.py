a = int(input("Enter a number: "))

if not a % 2 and not a % 3:
    print("a % 2 and 3")

if not a % 2 and not a % 5:
    print("a % 2 and 5")

if a <= 10 or a >= 50:
    print("a is not in range (10, 50)")  # [10, 50)

if a > 10 and a < 50:
    print("a is in range (10, 50)")
