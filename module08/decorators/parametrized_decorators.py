def hello_decorator(num):
    """Simple decorator function that supports parameters"""

    def inner_func(func):
        def wrapper(*args, **kwargs):
            """Simple decorator wrapper function"""
            result = func(*args, **kwargs)
            result = result + num
            return result

        return wrapper

    return inner_func


@hello_decorator(100)
def add(a, b):
    """Simple function that returns sum of two numbers"""
    return a + b


@hello_decorator(200)
def multiply(a, b):
    """Simple function that returns multiplication of two numbers"""
    return a * b


if __name__ == "__main__":
    output1 = add(2, 2)
    print("Result:: ", output1)
    print("=" * 25)

    output2 = multiply(4, 2)
    print("Result:: ", output2)
