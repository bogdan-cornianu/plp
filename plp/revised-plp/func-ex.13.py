__author__ = 'bogdan.cornianu'


def memoize(function):
    cache = {}

    def inner(value):
        if value in cache:
            return cache[value]
        result = function(value)
        cache[value] = result
        return result
    return inner


@memoize
def recursive_fibonacci_for(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return recursive_fibonacci_for(n - 1) + recursive_fibonacci_for(n - 2)

print recursive_fibonacci_for(input("Number: "))

#0.001888 - recursive fibonacci without memoization
#0.000319 - recursive fibonacci with memoization