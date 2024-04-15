# print numbers of even squares from start to end with step

# show why we need if, for
# show why we need functions
# explain diff btw arguments and params
# show default params
# show return by adding list
# explain named keywords
def print_even_squares(start, end, step=1): # signature
    count = 1
    for i in range(start, end, step):
        if i % 2 == 0:
            print(f"#{count} : {i} : {i ** 2}")
            count += 1

print_even_squares(1,10)
print_even_squares(start=1,10)
print_even_squares(1, start=10) # not named params first