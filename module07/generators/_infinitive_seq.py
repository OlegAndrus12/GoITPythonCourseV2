def fibonacci():
    # Initializing the first fibonacci numbers
    a, b = 0, 1
    
    # We need the generator to yield fibonacci values one by one
    # until the limit is reached.
    while True:
        yield a
        # As you can notice here, the yield takes place
        # prior to calculating the upcoming number, so when the
        # generator is resumed, it will return back to this point
        # and resumes from there.
        a, b = b, a+b

f = fibonacci()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
