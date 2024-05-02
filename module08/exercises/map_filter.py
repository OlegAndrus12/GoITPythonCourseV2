lst = [1, 4, 9, 11, 400]
a = filter(lambda x: x < 100, map(lambda x: x**2, lst))

print(list(a))
