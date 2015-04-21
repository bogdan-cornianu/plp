__author__ = 'bogdan.cornianu'


# Ex. 8
def sort_values(values):
    length = len(values)

    for i in range(length):
        for j in range(length - i - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]

    return values

print sort_values([3, 2, 7, 6, 9, 5, 4, 1, 8])
