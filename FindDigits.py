__author__ = 'bogdan.cornianu'
from sys import stdin

number_of_cases = int(stdin.readline())

for line in range(number_of_cases):
    number = stdin.readline()
    counter = 0

    for digit in str(number).strip():
        if int(digit) and int(number) % int(digit) == 0:
            counter += 1

    print counter