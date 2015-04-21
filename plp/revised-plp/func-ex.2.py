__author__ = 'bogdan.cornianu'
from .func_ex_1 import is_prime

# Ex. 2
def get_prime_numbers_upto(max_number):
    return filter(is_prime, range(1, max_number))

print get_prime_numbers_upto(input("Max number: "))
