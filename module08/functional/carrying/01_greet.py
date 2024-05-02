def greeting_simple(name, msg):
    return f"{name} - {msg}"


print(greeting_simple("Boris", "Go to work!"))
print(greeting_simple("Boris", "Go to home!"))


def greeting(name):
    def message(msg):
        return f"{name} - {msg}"

    return message


msg_for_boris = greeting("Boris")("Go to home!")  # chain of calls is carrying
print(msg_for_boris)
