"""
Write a function to compute the sum of digits of each number of a given list.
assert sum_of_digits([10,2,56])==14
"""


def sum_of_digits(numbers):
    """
    :param numbers: list of numbers
    :return: sum of digits of each number
    """
    return sum(sum(map(int, str(number))) for number in numbers)


if __name__ == '__main__':
    print(sum_of_digits([10, 2, 56]))
    print(sum_of_digits([10, 2, 56, 100, 1000]))
    print(sum_of_digits([10, 2, 56, 100, 1000, 10000]))
    print(sum_of_digits([10, 2, 56, 100, 1000, 10000, 100000]))
    print(sum_of_digits([10, 2, 56, 100, 1000, 10000, 100000, 1000000]))
    print(sum_of_digits([10, 2, 56, 100, 1000, 10000, 100000, 1000000, 10000000]))
    print(sum_of_digits([10, 2, 56, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]))
    print(sum_of_digits([10, 2, 56, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]))
    print(sum_of_digits([10, 2, 56, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000]))
    print(sum_of_digits([10, 2, 56, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000]))
    print(sum_of_digits([10, 2, 56, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000, 1000000000000]))
    print(sum_of_digits([10, 2, 56, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000, 1000000000000, 1