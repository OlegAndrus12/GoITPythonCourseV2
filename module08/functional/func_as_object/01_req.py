# Function as first class object

# Function can be saved in variable or another data structure


def mul(a, b):
    return a * b


f = mul
result = f(2, 3)
print(result)

field = {"a": 2, "b": 3, "ops": f}

result = field.get("ops")(field.get("a"), field.get("b"))
print(result)

result = field.get("ops")(2, 3)
print(result)
