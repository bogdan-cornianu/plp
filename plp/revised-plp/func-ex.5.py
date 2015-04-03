__author__ = 'bogdan.cornianu'


# Ex. 5
def filter_2(func, it):
    res = []
    for item in it:
        func_return = func(item)

        if func_return:
            res.append(func_return)

    return res


def test_func_filter_2(n):
    return n

print filter_2(test_func_filter_2, [False, True, False, True, True])