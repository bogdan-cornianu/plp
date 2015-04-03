__author__ = 'bogdan.cornianu'

word_dicts = {}
with open("res/words.txt", "r") as f:
    for line in f:
        for word in line.split():
            if word not in word_dicts:
                word_dicts[word] = 1
            else:
                word_dicts[word] += 1

for word in word_dicts:
    if word_dicts[word] == 1:
        print word