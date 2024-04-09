name = input(">>> ")
# old style
print("Hello, %s" % name)
# new style
print("Hello {}".format(name))
print(f"Hello {format}")


# all are the same
message = """
Never gonna give you up
Never gonna let you down
"""
mesage = "a"
message = "a"

# Python3 program to show the
# working of upper() function
text = "geeKs For geEkS"

# upper() function to convert
# string to upper case
print("\nConverted String:")
print(text.upper())

# lower() function to convert
# string to lower case
print("\nConverted String:")
print(text.lower())

# converts the first character to
# upper case and rest to lower case
print("\nConverted String:")
print(text.title())

# swaps the case of all characters in the string
# upper case character to lowercase and viceversa
print("\nConverted String:")
print(text.swapcase())

# convert the first character of a string to uppercase
print("\nConverted String:")
print(text.capitalize())

# original string never changes
print("\nOriginal String")
print(text)
