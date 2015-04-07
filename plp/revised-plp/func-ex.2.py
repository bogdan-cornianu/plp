__author__ = 'bogdan.cornianu'


def is_prime(number):
    for n in range(2, number):
        if number % n == 0:
            return False
    return True


# Ex. 2
def get_prime_numbers_upto(max_number):
    for number in range(1, max_number):
        if is_prime(number):
            print number

get_prime_numbers_upto(input("Max number: "))