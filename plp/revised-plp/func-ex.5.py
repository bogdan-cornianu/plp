__author__ = 'bogdan.cornianu'


# Ex. 5
def filter_2(function, iterable):
    return [item for item in iterable if function(item)]


def test_func_filter_2(n):
    return n % 2

filter_2(test_func_filter_2, [1, 2, 3, 4, 5])