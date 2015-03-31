__author__ = 'bogdan.cornianu'
import time


def time_slow(threshold):
    def inner_dec(func):
        def timer(*args, **kwargs):
            time_start = time.time()
            result = func(*args, **kwargs)
            time_end = time.time()
            print 'Execution took ' + str(time_end - time_start) + ' seconds for function ' + func.__name__  + \
                  ' with a threshold of ' + str(threshold)

            return result
        return timer
    return inner_dec


@time_slow(threshold=0.09)
def my_func(a, b='slow'):
    print a, b
    time.sleep(1)

my_func('a')