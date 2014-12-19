__author__ = 'bogdan.cornianu'
from sys import stdin

number_of_cases = int(stdin.readline())

for line in range(0, number_of_cases):
    number = stdin.readline()
    counter = 0

    for digit in list(str(number).strip()):
        if int(digit) > 0 and int(number) % int(digit) == 0:
            counter += 1

    print counter