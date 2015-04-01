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


def fibo_recurs(number):
    fibo_seq = []

    def recurs(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibo_recurs(n - 1) + fibo_recurs(n - 2)

    for idx in range(number):
        print idx

# fibo_iter()
fibo_recurs(input("Number: "))