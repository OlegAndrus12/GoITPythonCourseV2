# outer
def calculator(a, b, operation):
    message = "first level"

    # inner
    def add(a, b):
        nonlocal message
        message = "second level"
        print(message)
        return a + b

    def substract(a, b):
        return a - b

    if operation == "+":
        print(message)
        res = add(a, b)
        print(message)
        return res
    elif operation == "-":
        return substract(a, b)
    else:
        return "Incorrect operation"


a = calculator(1, 5, "+")
print(a)


# outside function
def outer():
    message = "local"

    # nested function
    def inner():
        # declare nonlocal variable
        nonlocal message

        message = "nonlocal"
        print("inner:", message)

    inner()
    print("outer:", message)


outer()
