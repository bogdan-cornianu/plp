__author__ = 'bogdan.cornianu'


def get_prime_numbers_upto():
    max_number = input("Max number: ")
    file = open("res/prime_nums.txt", "w")

    for idx in range(1, max_number):
        is_prime = True

        for n in range(2, idx):
            if idx % n == 0:
                is_prime = False
                break

        if is_prime:
            file.write(str(idx) + "\n")

    file.close()

get_prime_numbers_upto()

