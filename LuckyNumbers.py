__author__ = 'bogdan.cornianu'


def get_number_sum(n):
    psum = 0
    for b in str(n):
        psum += int(b)

    if psum > 1:
        return psum
    return 0

def is_prime(n):
    if n > 1:
        for nr in xrange(2, int(n**0.5)+1):
            if n % nr == 0:
                return False
    else:
        return False

    return True


def get_sum_of_squares(n):
    psum = 0
    for b in str(n):
        psum += (int(b) ** 2)
    return psum

tc_number = input()

for line in range(int(tc_number)):
    accum = 0
    interval = raw_input().split()
    for number in xrange(int(interval[0]), int(interval[1])):
        if len(str(number)) > 1:
            nsum = get_number_sum(number)
            ssum = get_sum_of_squares(number)

            if is_prime(nsum) and is_prime(ssum):
                accum += 1

    print accum