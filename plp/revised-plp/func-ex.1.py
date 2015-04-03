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

check_prime_number()