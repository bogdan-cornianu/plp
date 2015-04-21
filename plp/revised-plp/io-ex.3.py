from collections import Counter


def find_words_used_once_in(file_name):
    with open(file_name, "r") as f:
        counter = Counter(reduce(lambda x, y: x + y,
                                 [l.strip().split() for l in f.readlines()]))
    return filter(lambda w: counter[w] == 1, counter)


print find_words_used_once_in(raw_input("File name: "))
