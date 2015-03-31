__author__ = 'bogdan.cornianu'

import sys

try:
    input_dict = input('Input: ')

except NameError:
        print 'Not a dictionary.'
        sys.exit(0)


new_dict = {}


def is_tuple_assignable_as_key(t):
    for item in t:
        if type(item) not in [str, int]:
            return False

    return True

for k, v in input_dict.iteritems():
    type_of_value = type(v)

    if type_of_value in [str, int]:
        new_dict[v] = k

    elif type_of_value is tuple and is_tuple_assignable_as_key(v) is True:
        new_dict[v] = k
    else:
        print 'Swap is not possible.'
        sys.exit(0)


print 'Output: '
print new_dict