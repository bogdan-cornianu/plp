__author__ = 'bogdan.cornianu'


def get_numbers_from_files(number_of_files):
    numbers = []
    for n in range(number_of_files):
        with open(raw_input("File name: "), "r") as f:
            for line in f.readlines():
                numbers.append(int(line.strip()))
    return numbers


def write_numbers_to(file_name, numbers):
    with open(file_name, "w") as f:
        f.writelines(map(lambda n: str(n) + "\n", sorted(numbers)))


write_numbers_to(raw_input("Output file: "),
                 get_numbers_from_files(input("Number of files: ")))