__author__ = 'bogdan.cornianu'

n = input()
test_cases = [input() for _ in range(0, n)]

for x in test_cases:
    if x == 0:
        print 1
    elif x % 2 == 0:
        print pow(2, (x / 2 + 1)) - 1
    else:
        print pow(2, ((x + 1) / 2) + 1) - 2
