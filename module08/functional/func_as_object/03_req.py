# Function as first class object

# Function can be returned as a result of another function


def mul(a, b):
    return a * b


def add(a, b):
    return a + b


def ops(operator: str):
    if operator == "*":
        return mul
    elif operator == "+":
        return add
    else:
        raise ValueError("operator not supported")


try:
    f_mul = ops("*")  # f = mul
    result = f_mul(2, 4)
    print(result)
except ValueError:
    print("Can not execute operator *")

try:
    f_add = ops("+")
    result = f_add(2, 4)
    print(result)
except ValueError:
    print("Can not execute operator +")

try:
    f_div = ops("/")
    result = f_div(2, 4)
    print(result)
except ValueError:
    print("Can not execute operator /")
