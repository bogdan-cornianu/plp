__author__ = 'bogdan.cornianu'


# Ex. 1
print "".join(list(reversed(raw_input("Name: ").upper())))


# Ex. 2
def is_palindrome(number):
    if number <= 10:
        return False

    initial_number = number
    reversed_number = 0

    while number > 0:
        remainder = number % 10
        reversed_number = reversed_number * 10 + remainder
        number /= 10

    return initial_number == reversed_number


print is_palindrome(input("Number: "))


# Ex. 3
def all_palindromes_smaller_than(number):
    return filter(lambda n: is_palindrome(n), range(9, number))

print all_palindromes_smaller_than(input("Max number: "))

