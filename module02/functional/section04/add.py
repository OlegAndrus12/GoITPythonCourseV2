def add_recursion(max_number):
    # when to stop ?
    if max_number <= 0:
        return 0

    if max_number == 1:
        return 1

    return max_number + add_recursion(max_number - 1)


3 + 2 + 1 + 0
print(add_recursion(1000))

# f(4) + f(3) + f(2) + f(1) + f(0)

# 1 + 2 + 3 + ... + 10

# f(10) -> 10 + f(9)
# f(9) -> 9 + f(8)
# f(8) -> 8 + f(7)
# f(7) -> 7 + f(6)
# f(6) -> 6 + f(5)
# f(5) -> 5 + f(4)
# f(4) -> 4 + f(3)
# f(3) -> 3 + f(2)
# f(2) -> 2 + f(1)
# f(1) -> 1 + f()


def add(l):
    res = 0
    # iteration
    for element in l:
        res += element

    return res
