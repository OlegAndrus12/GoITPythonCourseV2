from time import time_ns

LIMIT = 1000000


def cubed(x):
    return x**3


start = time_ns()
print(f"Cube of 9 is {cubed(9)}")
print(f"Time taken for previous method : {(time_ns()-start)//1_000} ms")

################

start = time_ns()
lambda_cubed = lambda x: x**3
print(f"Cube of 9 is {lambda_cubed(9)}")
print(f"Time taken for previous lambda : {(time_ns()-start)//1_000} ms")

################

start = time_ns()
print(f"Cube of 9 is {(lambda x:x**3)(9)}")
print(f"Time taken for inline lambda : {(time_ns()-start)//1_000} ms")

################

start = time_ns()
squares = []

for i in range(LIMIT):
    squares.append(i**2)

print(f"Time taken for a for loop to generate squares: {(time_ns()-start)//1_000} ms")

################

start = time_ns()
squares = [i**2 for i in range(LIMIT)]
print(
    f"Time taken for list comprehension to generate squares : {(time_ns()-start)//1_000} ms"
)

################


start = time_ns()
# if you evaluate then it is slower
squares = map(lambda i: i**2, range(LIMIT))
print(
    f"Time taken for map and lambda function to generate squares : {(time_ns()-start)//1_000} ms"
)

################

start = time_ns()
evens = []
for i in range(LIMIT):
    if i % 2 == 0:
        evens.append(i)

print(f"Time taken for a for loop : {(time_ns()-start)//1_000} ms")

################
start = time_ns()
squares = list(filter(lambda i: i % 2 == 0, range(LIMIT)))
print(f"Time taken for filter : {(time_ns()-start)//1_000} ms")
