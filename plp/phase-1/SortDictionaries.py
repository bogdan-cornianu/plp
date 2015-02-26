__author__ = 'bogdan.cornianu'

# global scope variables
dict_list = []
sorted_dicts = []


def sort_dict():
    list_of_keys = []
    already_sorted_keys = []

    for dict_elem in dict_list:
        list_of_keys.append(get_smallest_key(dict_elem))

    sorted_keys = sort_keys(list_of_keys)
    for key in sorted_keys:
        if sorted_keys.count(key) > 1 and key not in already_sorted_keys:
            already_sorted_keys.append(key)
            for sorted_dictionary in sorted(find_dict_by_key(key)):
                sorted_dicts.append(sorted_dictionary)
        elif sorted_keys.count(key) == 1 and key not in already_sorted_keys:
            sorted_dicts.append(find_dict_by_key(key))


def find_dict_by_key(dict_key):
    found_dicts = []
    for dict_elem in dict_list:
        if dict_key in dict_elem.keys():
            found_dicts.append(dict_elem)
            if len(dict_elem.keys()) == 1 and dict_elem.keys().count(dict_key) == 1:
                return dict_elem

    return found_dicts


def get_smallest_key(input_dict):
    smallest_key = input_dict.keys()[0]
    for key in input_dict.keys():
        if key < smallest_key:
            smallest_key = key

    return smallest_key


# bubble sort the list of keys
def sort_keys(list_of_keys):
    for i in range(len(list_of_keys)):
        for j in range(len(list_of_keys)-1-i):
            if list_of_keys[j] > list_of_keys[j + 1]:
                list_of_keys[j], list_of_keys[j+1] = list_of_keys[j+1], list_of_keys[j]

    return list_of_keys

with open('tmp/dict_sort.input', 'r') as dict_file_in:
    dictionary = {}
    for line in dict_file_in:
        if line not in ['\n', '\r\n']:
            dictionary[line.split()[0]] = int(line.split()[1])

            if dictionary not in dict_list:
                dict_list.append(dictionary)
        else:
            dictionary = {}

    sort_dict()

with open('tmp/dict_sort.output', 'w') as dict_file_out:
    for dicts in sorted_dicts:
        dict_file_out.write(str(dict_list.index(dicts)) + " ")
