# 0 -> numbers are equal
# -1 -> first number is less than the second
# 1 -> first number is bigger than the second
from decimal import Decimal

print(Decimal("1.2").compare(Decimal("1.1")))
print(Decimal("1.0").compare(Decimal("1.1")))
print(Decimal("1.0").compare(Decimal("1.0")))

print(0.1 + 0.2 == 0.3)
num1 = Decimal("0.1") + Decimal("0.2")
num2 = Decimal("0.3")
print(num1.compare(num2))
