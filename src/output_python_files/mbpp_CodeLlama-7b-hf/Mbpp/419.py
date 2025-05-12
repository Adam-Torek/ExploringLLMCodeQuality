"""
Write a function to round every number of a given list of numbers and print the total sum multiplied by the length of the list.
assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])==243
"""


def round_and_sum(numbers):
    """
    :param numbers: list of numbers
    :return: sum of rounded numbers
    """
    return sum(round(number) for number in numbers)


if __name__ == '__main__':
    print(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]))
    print(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50, 17.50]))
    print(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50, 17.50, 17.50]))
    print(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50, 17.50, 17.50, 17.50]))
    print(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50, 17.50, 17.50, 17.50, 17.50]))
    print(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50, 17.50, 17.50, 17.50, 17.50, 17.50]))
    print(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50, 17.50, 17.50, 17.50, 17.50, 17.50, 17.50]))
    print(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50, 17.50, 17.50, 17.50, 17.50, 17.50, 17.50, 17.50]))
    print(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50, 17.50, 17.50, 17.50, 17.50, 17.50, 17.50, 17.50, 17.50]))
    print(