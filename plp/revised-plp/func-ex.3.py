__author__ = 'bogdan.cornianu'


# Ex. 3
def iterative_fibonacci(number):
    def compute():
        a, b = 0, 1
        for i in range(number):
            a, b = b, a + b
            yield a

    return [n for n in compute()]


def recursive_fibonacci(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    return recursive_fibonacci(number - 1) + recursive_fibonacci(number - 2)

print iterative_fibonacci(input("Number: "))
print recursive_fibonacci(input("Number: "))