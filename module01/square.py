import math


a = int(input("Enter a side >>> "))
b = int(input("Enter b side >>> "))
c = int(input("Enter c side >>> "))


print(a, b, c)

P = a + b + c

p = P / 2

S = math.sqrt(p * (p - a) * (p - b) * (p - c))

print("Square is ", S)
print("Square is {}".format(S))
print(f"Square is {S}")
