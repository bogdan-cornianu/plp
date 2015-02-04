__author__ = 'bogdan.cornianu'


def insertion_sort(array, length):
    cell = array[len(array) - 1]
    idx = length - 1

    while idx >= 0:
        if idx == 0 and array[idx] > cell:
            array[idx] = cell
            break
        elif array[idx - 1] > cell:
            array[idx] = array[idx - 1]
        else:
            array[idx] = cell
            break

        idx -= 1
        print ' '.join(str(char) for char in array)
    print ' '.join(str(char) for char in array)

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertion_sort(ar, m)