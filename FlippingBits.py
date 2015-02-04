__author__ = 'bogdan.cornianu'

n = input()
test_cases = [input() for _ in range(0, n)]

for x in test_cases:
    print int(pow(2, 32) + ~x)