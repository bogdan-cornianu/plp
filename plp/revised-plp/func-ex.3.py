__author__ = 'bogdan.cornianu'


# Ex. 3
def fibo_iter():
    number = input("Number: ")
    a, b = 0, 1

    for i in range(number):
        a, b = b, a + b
        print a


def fibo_recurs(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_recurs(n - 1) + fibo_recurs(n - 2)

fibo_iter()
print fibo_recurs(input("Number: "))