from time import time, sleep


def measure(func):
    def wrapper(*args, **kwargs):
        t = time()
        res = func(*args, **kwargs)
        print(func.__name__, "took", time() - t)
        return res

    return wrapper


@measure
def sleepy_function(sleep_time):
    sleep(sleep_time)
    return 10


print(sleepy_function(0.3))
sleepy_function(0.5)
