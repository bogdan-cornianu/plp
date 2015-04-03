__author__ = 'bogdan.cornianu'


def memoiz_deco(func):

    def inner_func(val, cache={}):
        if val in cache:
            return cache[val]

        res = func(val)
        cache[val] = res

        return res

    return inner_func


@memoiz_deco
def fibo_recurs(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_recurs(n - 1) + fibo_recurs(n - 2)

print fibo_recurs(input("Number: "))

#0.001888 - fibo recursive without memoization
#0.000319 - fibo recursive with memoization