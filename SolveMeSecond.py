__author__ = 'bogdan.cornianu'


def solve_me_second(first, second):
    return first + second

n = int(raw_input())  # faster than n = input() , since input() executes the line as python command
for i in range(0, n):
    a, b = raw_input().split()
    a, b = int(a), int(b)
    res = solve_me_second(a, b)
    print res