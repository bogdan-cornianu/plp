__author__ = 'bogdan.cornianu'


def merge_objects(obj1, obj2):
    result = {}

    for key1, value1 in obj1.iteritems():
        for key2, value2 in obj2.iteritems():
            if key1 == key2:
                if type(value1) == type(value2) and type(value1) is set:
                    result[key1] = value1.union(value2)
                elif type(value1) == type(value2) and type(value1) is not dict:
                    result[key1] = value1 + value2
                elif type(value1) == type(value2) and type(value1) is dict:
                    new_dict = {}
                    for key3, value3 in value1.iteritems():
                        for key4, value4 in value2.iteritems():
                            new_dict[key3] = value3 + value4
                    result[key1] = new_dict
                else:
                    result[key1] = (value1, value2)

    return result

a = {'x': [1, 2, 3], 'y': 1, 'z': set([1, 2, 3]), 'w': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]}
b = {'x': [4, 5, 6], 'y': 4, 'z': set([4, 2, 3]), 'w': 'asdf', 't': {'a': [3, 2]}, 'm': "wer"}

print merge_objects(a, b)