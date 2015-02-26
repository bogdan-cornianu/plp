__author__ = 'bogdan.cornianu'
import operator

dict_list = []
sorted_dicts = []


def sort_dict():
    tmp_dict = []
    list_of_keys = []

    for dict_elem in dict_list:
        list_of_keys.append(get_smallest_key(dict_elem))

    print sort_keys(list_of_keys)
    # for dict_elem in dict_list:
    #     tmp_dict.append(sorted(dict_elem, key=lambda keyname: keyname[0]))
    #
    # for dict_item in sorted(tmp_dict):
    #     for elem in dict_list:
    #         if dict_item == elem.keys() and elem not in sorted_dicts:
    #             sorted_dicts.append(elem)

    # print sorted_dicts


def get_smallest_key(input_dict):
    smallest_key = input_dict.keys()[0]
    for key in input_dict.keys():
        if key < smallest_key:
            smallest_key = key

    return smallest_key


#bubble sort
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

    print dict_list
    sort_dict()

with open('tmp/dict_sort.output', 'w') as dict_file_out:
    for dicts in sorted_dicts:
        pass
        dict_file_out.write(str(dict_list.index(dicts)) + " ")
