from time import time
import resource


def read_file_yield(filename):
    text_file = open(filename, "r")
    while True:
        line = text_file.readline()
        if not line:
            text_file.close()
            break
        yield line


start = time()
data = read_file_yield("data.txt")

res = []
for line in data:
    res.append(line)
print((time() - start) * 1000)

print("Peak Memory Usage =", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)


def read_file(filename):
    text_file = open(filename, "r")
    lines = text_file.readlines()
    text_file.close()
    return lines


start = time()
data = read_file("data.txt")
print((time() - start) * 1000)

print("Peak Memory Usage =", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
