__author__ = 'bogdan.cornianu'


number_of_files = input("Number of files: ")
numbers = set()

for n in range(number_of_files):
    input_file = input("File path: ")
    with open(input_file, "r") as f:
        for line in f:
            numbers.add(int(line))

with open("res/sorted_nums.txt", "w") as output_file:
    for number in sorted(numbers):
        output_file.write(str(number) + "\n")