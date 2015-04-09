__author__ = 'bogdan.cornianu'


# Ex. 7
def map_function(n):
    return (n * n) - 1


def filter_function(n):
    return n % 3 == 0


def reduce_function(a, b):
    return a + b


def sum_of_numbers(number):
    return reduce(reduce_function,
                  filter(filter_function, map(map_function, range(1, number))))

sum_of_numbers(input("Number: "))