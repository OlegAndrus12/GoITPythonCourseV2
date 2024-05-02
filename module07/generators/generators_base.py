"""
To recap, iterators are objects that can be iterated on, and generators are special functions
that leverage lazy evaluation. Implementing your own iterator means you must create an __iter__()
and __next__() method, whereas a generator can be implemented using the yield keyword in
a Python function or comprehension.

You may prefer to use a custom iterator over a generator when you require an object with complex
state-maintaining behavior or if you wish to expose other methods beyond __next__(), __iter__(),
and __init__(). On the other hand, a generator may be preferable when dealing with large sets
of data since they do not store their contents in memory or when it is not necessary to implement
an iterator.

"""


def yield_multiple_statments():
    yield "This is the first statment"
    yield "This is the second statement"
    yield "This is the third statement"
    yield "This is the last statement. Don't call next again!"


example = yield_multiple_statments()
print(next(example))
print(next(example))
print(next(example))
print(next(example))
print(next(example))

(item for item in [1, 2, 3, 4])  # Generator expression
[item for item in [1, 2, 3, 4]]  # List comprehension
