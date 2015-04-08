__author__ = 'bogdan.cornianu'


def sum_of_numbers_in(file_name):
    with open(file_name, "r") as f:
        return sum(map(int, f.readlines()))

print sum_of_numbers_in(raw_input("File name: "))