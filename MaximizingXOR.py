__author__ = 'bogdan.cornianu'

l = input()
r = input()

x = l
res = 0
number_list = []
while l <= x <= r:
    number_list.append(x)
    x += 1

for i in number_list:
    for j in number_list:
        if i ^ j > res:
            res = i ^ j

print res