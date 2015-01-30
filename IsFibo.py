__author__ = 'bogdan.cornianu'
from sys import stdin


def fib(n):
    a, b = 0, 1
    fib_list = []
    while a < n:
        fib_list.append(a)
        a, b = b, a + b

    return fib_list

number_of_cases = int(stdin.readline())

for line in range(number_of_cases):
    number = int(stdin.readline())

    if fib(number + 1).count(number) == 0:
        print 'IsNotFibo'
    else:
        print 'IsFibo'