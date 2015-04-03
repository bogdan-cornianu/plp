__author__ = 'bogdan.cornianu'


num_sum = 0
with open("res/numbers.txt", "r") as f:
    for line in f:
        num_sum += int(line)

print "Sum is: " + str(num_sum)