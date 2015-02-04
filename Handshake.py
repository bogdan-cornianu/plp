__author__ = 'bogdan.cornianu'

n = input()
test_cases = [input() for _ in range(0, n)]

for handshake in test_cases:
    print handshake * (handshake - 1) / 2