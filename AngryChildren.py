__author__ = 'bogdan.cornianu'
from sys import stdin


number_of_cases = int(stdin.readline())
k = int(stdin.readline())

list_of_numbers = []

for line in range(number_of_cases):
    list_of_numbers.append(int(stdin.readline()))

list_of_numbers.sort()
number_of_candies = len(list_of_numbers)
list_of_candidates = []

i = 0
while i < number_of_candies / k:
    temp_list = list_of_numbers[:k]
    del list_of_numbers[:k-1]
    list_of_candidates.append(max(temp_list) - min(temp_list))
    i += 1

print min(list_of_candidates)