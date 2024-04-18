import math


a = input("Enter a side >>> ")
b = input("Enter b side >>> ")
c = input("Enter c side >>> ")



print(a, b, c)

P = a + b + c

p = P / 2


res = p * p - a * p - b * p - c
S = math.sqrt(res)

print("Square is ", S)
print("Square is {}".format(S))
print(f"Square is {S}")
