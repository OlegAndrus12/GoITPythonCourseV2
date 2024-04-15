message = "Hello Mr."


def greet(name):
    age = 2
    print(locals())
    print(message, name)


def greet2(name):
    message = "Good morning! "
    print(message, name)


def greet3(name):
    global message
    message = "Good morning! "
    print(message, name)


greet("Oleh")
greet2("Oleh")
print(message)
greet3("Oleh")
print(message)

print(globals())
