__author__ = 'bogdan.cornianu'
import time


def time_slow(func):
    def timer(*args, **kwargs):
        time_start = time.time()
        result = func(*args, **kwargs)
        time_end = time.time()
        print 'Execution took ' + str(time_end - time_start) + ' seconds for function ' + func.__name__

        return result
    return timer


@time_slow
def my_func(a, b='slow'):
    print a, b
    time.sleep(1)

my_func('a')