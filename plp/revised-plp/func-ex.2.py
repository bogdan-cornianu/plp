__author__ = 'bogdan.cornianu'


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

get_prime_numbers_upto()