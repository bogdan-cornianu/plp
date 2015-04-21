__author__ = 'bogdan.cornianu'


def is_prime(number):
    for n in range(2, number):
        if number % n == 0:
            return False
    return True


def write_prime_numbers_into_file(max_number, file_name):
    with open(file_name, "w") as f:
        f.writelines(map(lambda s: str(s) + "\n",
                         filter(lambda n: n < max_number and is_prime(n),
                                range(max_number))))

write_prime_numbers_into_file(input("Max number: "), raw_input("File name: "))
