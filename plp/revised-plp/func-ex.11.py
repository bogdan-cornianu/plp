__author__ = 'bogdan.cornianu'
import time


def timer(func):
    def wrapper():
        start_time = time.time()
        try:
            result = func()
        finally:
            print "Execution time for " + func.__name__ + " is {:.5}".format(time.time() - start_time) + " seconds."
        return result
    return wrapper


@timer
def test_func_1():
    time.sleep(1)

test_func_1()
