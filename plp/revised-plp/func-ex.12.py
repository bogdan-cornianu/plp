__author__ = 'bogdan.cornianu'
import time


def timer(func):

    def inner_func():
        start_time = time.time()
        result = func()
        duration = time.time() - start_time

        print "Execution time for " + func.__name__ + " is {:.5}".format(duration) + " seconds."
        timer.counter += duration

        return result

    return inner_func

timer.counter = 0


@timer
def test_func_1():
    time.sleep(1)


@timer
def test_func_2():
    time.sleep(1)


@timer
def test_func_3():
    time.sleep(1)


@timer
def test_func_4():
    time.sleep(1)


test_func_1()
test_func_2()
test_func_3()
test_func_4()


print "------------------------"
print "Total execution time for decorated functions is {:.5}".format(timer.counter) + " seconds."