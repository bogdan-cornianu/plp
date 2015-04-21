__author__ = 'bogdan.cornianu'


# Ex. 4
def map_2(function, iterable):
    return list((function(item) for item in iterable))


def test_map_2(n):
    return n

print map_2(test_map_2, {1: 'a', 2: 'b'})
