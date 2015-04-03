__author__ = 'bogdan.cornianu'


# Ex. 7
def func_map(n):
    return (n * n) - 1


def func_filter(n):
    if n % 3 == 0:
        return True

    return False


def func_reduce(a, b):
    return a + b


def compute():
    max_value = input("Max value: ")
    sum_of_ns = 0
    seed = 1
    prev_sum = 0
    accum = []

    while sum_of_ns < max_value:
        accum.append(seed)
        prev_sum = sum_of_ns

        mapped = map(func_map, accum)
        filtered = filter(func_filter, mapped)
        sum_of_ns = reduce(func_reduce, filtered)

        seed += 1

    print sum_of_ns if sum_of_ns < max_value else prev_sum

compute()