__author__ = 'bogdan.cornianu'


def flatten(list_a, list_b, max_depth):
    return flatten_list(list_a, max_depth) + flatten_list(list_b, max_depth)


def flatten_list(input_list, depth):
    result = []

    for list_item in input_list:
        if isinstance(list_item, list) and depth > 0:
            result += flatten_list(list_item, depth - 1)
        else:
            result.append(list_item)

    return result

print flatten([1, [2, 3, [9, 10, [11, 12, [13, 15]]]]], [4, [5, 6]], 1)