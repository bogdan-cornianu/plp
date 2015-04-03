__author__ = 'bogdan.cornianu'
import time


def timer(func):

    def inner_func():
        start_time = time.time()
        res = func()
        end_time = time.time()

        print "Execution time for " + func.__name__ + " is {:.5}".format(end_time - start_time) + " seconds."

        return res

    return inner_func


@timer
def test_func_1():
    time.sleep(1)

test_func_1()
