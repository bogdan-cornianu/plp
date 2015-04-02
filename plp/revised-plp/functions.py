__author__ = 'bogdan.cornianu'


# Ex. 1
def check_prime_number():
    number = input("Number: ")
    is_prime = True

    for n in range(2, number):
        if number % n == 0:
            is_prime = False
            break

    if is_prime:
        print str(number) + ' is prime.'
    else:
        print str(number) + ' is NOT prime.'

#check_prime_number()


# Ex. 2
def get_prime_numbers_upto():
    max_number = input("Max number: ")

    for idx in range(1, max_number):
        is_prime = True

        for n in range(2, idx):
            if idx % n == 0:
                is_prime = False
                break

        if is_prime:
            print idx

# get_prime_numbers_upto()


# Ex. 3
def fibo_iter():
    number = input("Number: ")
    a, b = 0, 1

    for i in range(number):
        a, b = b, a + b
        print a


def fibo_recurs(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_recurs(n - 1) + fibo_recurs(n - 2)

# fibo_iter()
#print fibo_recurs(input("Number: "))


# Ex. 4
def map_2(func, it):
    res = []
    for item in it:
        res.append(func(item))

    return res


def test_map_2(n):
    return n

#print map_2(test_map_2, {1: 'a', 2: 'b'})


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

#print filter_2(test_func_filter_2, [False, True, False, True, True])


# Ex. 6
def reduce_2(func, it, init):
    accum = init
    for item in it:
        accum = func(accum, item)

    return accum


def test_reduce_2(a, b):
    return a + b

#print reduce_2(test_reduce_2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)


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

#compute()


# Ex. 8
def sort_values(values):
    length = len(values)

    for i in range(length):
        for j in range(length - i - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]

    return values

#print sort_values([3, 2, 7, 6, 9, 5, 4, 1, 8])


# Ex. 9
def search_for_value(sorted_values, value):

    def binary_search(values_list, key, idx_min, idx_max):
        if idx_max < idx_min:
            return -1
        else:
            idx_mid = (idx_min + idx_max) / 2

            if values_list[idx_mid] > key:
                return binary_search(values_list, key, idx_min, idx_mid - 1)
            elif values_list[idx_mid] < key:
                return binary_search(values_list, key, idx_mid + 1, idx_max)
            else:
                return idx_mid

    find_at_pos = binary_search(sorted_values, value, 0, len(sorted_values) - 1)

    if find_at_pos > -1:
        return "Found {0} at position {1}.".format(value, find_at_pos)
    else:
        return "Value not found."


print search_for_value([1, 3, 4, 6, 8, 9, 11], 8)
