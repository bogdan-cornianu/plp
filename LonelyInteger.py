__author__ = 'bogdan.cornianu'


def lonely_integer(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i
    return 0

if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonely_integer(b)