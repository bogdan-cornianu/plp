__author__ = 'bogdan.cornianu'


# Ex. 7
def map_function(n):
    return (n * n) - 1


def filter_function(n):
    if n % 3 == 0:
        return True

    return False


def reduce_function(a, b):
    return a + b


def sum_of_numbers(number):
    return reduce(reduce_function, filter(filter_function, map(map_function, range(1, number))))

print sum_of_numbers(input("Number: "))