__author__ = 'bogdan.cornianu'
import time


def timer(function):
    def inner():
        result = None
        start_time = time.time()
        try:
            result = function()
        finally:
            duration = time.time() - start_time
            print "Execution time for " + function.__name__ + \
                  " is {:.5}".format(duration) + " seconds."
            try:
                timer.counter += duration
            except AttributeError:
                timer.counter = 1
        return result
    return inner


@timer
def test_function_1():
    time.sleep(1)


@timer
def test_function_2():
    time.sleep(1)


@timer
def test_function_3():
    time.sleep(1)


@timer
def test_function_4():
    time.sleep(1)


test_function_1()
test_function_2()
test_function_3()
test_function_4()


print "------------------------"
print "Total time for decorated functions is {:.5}".format(timer.counter) + \
      " seconds."