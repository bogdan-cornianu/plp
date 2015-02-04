__author__ = 'bogdan.cornianu'
from sys import stdin

number_of_cases = int(stdin.readline())

for line in range(number_of_cases):
    res = 0
    prev = ''

    for x in stdin.readline():
        if x != '\n':
            if x == prev:
                res += 1
            else:
                prev = x
    print res