__author__ = 'bogdan.cornianu'


# Ex. 9
def search_for_value(sorted_values, value):

    def binary_search(values_list, key, idx_min, idx_max):
        if idx_max < idx_min:
            return -1
        else:
            idx_mid = (idx_min + idx_max) / 2

            if values_list[idx_mid] > key:
                return binary_search(values_list, key, idx_min, idx_mid - 1)
            elif values_list[idx_mid] < key:
                return binary_search(values_list, key, idx_mid + 1, idx_max)
            else:
                return idx_mid

    find_at_pos = binary_search(sorted_values, value, 0, len(sorted_values) - 1)

    if find_at_pos > -1:
        return "Found {0} at position {1}.".format(value, find_at_pos)
    else:
        return "Value not found."


print search_for_value([1, 3, 4, 6, 8, 9, 11], 8)
