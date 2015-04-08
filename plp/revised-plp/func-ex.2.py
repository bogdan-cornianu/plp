__author__ = 'bogdan.cornianu'


def is_prime(number):
    for n in range(2, number):
        if number % n == 0:
            return False
    return True


# Ex. 2
def get_prime_numbers_upto(max_number):
    return filter(lambda n: is_prime(n), range(1, max_number))

print get_prime_numbers_upto(input("Max number: "))