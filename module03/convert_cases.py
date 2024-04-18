# write a function to convert from pythonCase camelCase, PascalCase

# Python3 program to convert string
# from camel case to snake case


def snake_to_camel(s):
    # Python3 code to demonstrate working of
    # Convert Snake Case String to Camel Case
    # Using split() + join() + title() + generator expression

    # initializing string
    test_str = "geeksforgeeks_is_best"

    # printing original string
    print("The original string is : " + str(test_str))

    # split underscore using split
    temp = test_str.split("_")

    # joining result
    res = temp[0] + "".join(ele.title() for ele in temp[1:])

    # printing result
    print("The camel case string is : " + str(res))


def camel_to_snake(str):
    res = ""
    for i in str:
        if i.isupper():
            res += "_" + i.lower()
        else:
            res += i
    return res[1:]


# Driver code
str = "GeeksForGeeks"
print(camel_to_snake(str))
