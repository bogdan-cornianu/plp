__author__ = 'bogdan.cornianu'


# Ex. 6
def reduce_2(function, iterable, init):
    accumulator = init
    for item in iterable:
        accumulator = function(accumulator, item)
    return accumulator


def test_reduce_2(a, b):
    return a + b

reduce_2(test_reduce_2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
