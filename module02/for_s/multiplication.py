# outer loop
for i in range(1, 6):
    print("Multiplication table of:", i)
    count = 1
    # inner loop to print multiplication table of current number
    while count < 11:
        print(i * count, end=" ")
        count = count + 1
    print("\n")
