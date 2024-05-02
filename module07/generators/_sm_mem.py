import sys

nums_squared_lc = [i ** 2 for i in range(10000)]

print(sys.getsizeof(nums_squared_lc), "bytes")

nums_squared_gc = (i ** 2 for i in range(10000))
print(sys.getsizeof(nums_squared_gc), "bytes")
