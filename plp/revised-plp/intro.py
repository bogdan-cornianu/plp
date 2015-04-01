__author__ = 'bogdan.cornianu'


# Ex. 1
# my_name = raw_input("What's my name? ")
# print "My name is " + my_name[::-1].upper()

# Ex. 2
# number = input("Number = ")
# tmp = number
# stack = []
#
# while tmp >= 1:
#     stack.append(tmp % 10)
#     tmp /= 10
#
# is_palindrome = True
#
# while len(stack) > 0:
#     if stack.pop() != (number % 10):
#         is_palindrome = False
#
#     number /= 10
#
# print is_palindrome

# Ex. 3
max_number = input("Max number = ")

stack = []

for idx in range(1, max_number):
    if idx > 9:
        tmp = idx
        initial = idx

        while tmp >= 1:
            stack.append(tmp % 10)
            tmp /= 10

        is_palindrome = True

        while len(stack) > 0:
            if stack.pop() != (idx % 10):
                is_palindrome = False

            idx /= 10

        if is_palindrome:
            print initial
