message = "here i am"


# outside function
def outer():
    message = "local"

    # nested function
    def inner():
        # declare nonlocal variable
        nonlocal message  # change to global
        message = "nonlocal2222"
        print("inner:", message)

    inner()
    print("outer:", message)


outer()
print(message)
