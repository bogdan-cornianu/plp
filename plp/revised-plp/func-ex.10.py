__author__ = 'bogdan.cornianu'


def a():
    a.counter += 1
    return a.counter

a.counter = -1

print a()
print a()
print a()