res = {i: i**2 for i in range(100) if i % 2 == 0}
print(res)

# 17 list comprehension problems in python

fruits = ["mango", "kiwi", "strawberry", "guava", "pineapple", "mandarin orange"]

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]
number.from_bytes()
# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())

# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

# Exercise 5 - make a list that contains each fruit with more than 5 characters

# Exercise 6 - make a list that contains each fruit with exactly 5 characters

# Exercise 7 - Make a list that contains fruits that have less than 5 characters

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five.

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.

uppercased_fruits = [s.upper() for s in fruits]

capitalized_fruits = [f.capitalize() for f in fruits]

fruits_with_more_than_two_vowels_which_are_not_same = [
    f for f in fruits if len([True for v in ["a", "e", "i", "o", "u"] if v in f]) > 2
]

fruits_with_only_two_vowels = [
    f for f in fruits if len([True for s in f if s in ["a", "e", "i", "o", "u"]]) == 2
]

fruit_with_more_than_5_characters = [f for f in fruits if len(f) > 5]

fruit_with_exactly_5_characters = [f for f in fruits if len(f) == 5]

fruit_with_less_than_5_characters = [f for f in fruits if len(f) < 5]

number_of_character_in_each_fruit = [len(f) for f in fruits]

fruits_with_letter_a = [f for f in fruits if "a" in f]

even_numbers = [n for n in numbers if n % 2 == 0]

odd_numbers = [n for n in numbers if n % 2 == 1]

positive_numbers = [n for n in numbers if int(n) > 0]

negative_numbers = [n for n in numbers if n < 0]

two_or_more_numerals = [n for n in numbers if n > 9 or n < -9]

numbers_squared = [n**2 for n in numbers]

odd_negative_numbers = [n for n in numbers if n < 0 and n % 2 == 1]

numbers_plus_5 = [n + 5 for n in numbers]

primes = [
    num
    for num in numbers
    if num > 1
    if not 0 in list(map(lambda x: num % x, list(range(2, num))))
]
