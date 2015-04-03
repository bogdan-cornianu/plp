__author__ = 'bogdan.cornianu'


# Ex. 6
def reduce_2(func, it, init):
    accum = init
    for item in it:
        accum = func(accum, item)

    return accum


def test_reduce_2(a, b):
    return a + b

print reduce_2(test_reduce_2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
