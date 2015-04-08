__author__ = 'bogdan.cornianu'


def a():
    try:
        a.counter += 1
    except AttributeError:
        a.counter = 1
    finally:
        return a.counter

print a()
print a()
print a()
