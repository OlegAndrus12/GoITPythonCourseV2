# args = tuple arguments
# kwargs = dict keyword arguments


def add(a, b, *args):
    res = a + b
    for number in args:
        res += number

    return res


res = add(1, 2, 5, 6, 7, 8, 1221)


def intro(firstname, *args, **kwargs):
    print(kwargs)
    print(args)

    print("firstname", firstname)

    for key, value in kwargs.items():
        print(key, value)


intro(
    "Oleksandr",
    "12312",
    True,
    1231,
    last_name="Holodetskyi",
    age=18,
    school="GoIT",
)
