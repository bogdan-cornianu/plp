__author__ = 'bogdan.cornianu'


# Ex. 1
def is_prime(number):
    for n in range(2, number):
        if number % n == 0:
            return False
    return True


print is_prime(input("Number: "))