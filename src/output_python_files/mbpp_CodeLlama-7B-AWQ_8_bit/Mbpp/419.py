"""
Write a function to round every number of a given list of numbers and print the total sum multiplied by the length of the list.
assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])==243
"""


def round_and_sum(numbers):
    """
    :param numbers: list of numbers
    :return: sum of rounded numbers
    """
    total = 0
    for number in numbers:
        total += round(number)
    return total


if __name__ == '__main__':
    print(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]))
    print(round_and_sum([1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.10]))
    print(round_and_sum([-1.2, -2.3, -3.4, -4.5, -5.6, -6.7, -7.8, -8.9, -9.10]))
    print(round_and_sum([-1.2, -2.3, -3.4, -4.5, -5.6, -6.7, -7.8, -8.9, -9.10, 10.10]))
    print(round_and_sum([-1.2, -2.3, -3.4, -4.5, -5.6, -6.7, -7.8, -8.9, -9.10, 10.10, 11.10]))
    print(round_and_sum([-1.2, -2.3, -3.4, -4.5, -5.6, -6.7, -7.8, -8.9, -9.10, 10.10, 11.10, 12.10]))
    print(round_and_sum([-1.2, -2.3, -3.4, -4.5, -5.6, -6.7, -7.8, -8.9, -9.10, 10.10, 11.10, 12.10, 13.10]))
    print(round_and_sum([-1.2, -2.3, -3.4, -4.5, -5.6, -6.7, -7.8, -8.9, -9.10, 10.10, 11.10, 12.10, 13.10, 14.10]))
    print(round_and_sum([-1.2, -2.3, -3.4, -4.5, -5.6, -6.7, -7.8, -8.9, -9.10, 10.10, 11.10, 12.10, 13.10, 14.10, 15.10]))
    print(round_and_sum([-1.2, -2.3, -3.4, -4.5, -5.6, -6.7, -7.8, -8.9, -9.10, 10.10, 11.10, 12.10, 13.10, 14.10, 15.10, 16.10]))
    print(round_and_sum([-1.2, -2.3, -3.4, -4.5, -5.6, -6.7, -7.8, -8.9, -9.10, 10.10, 11.10, 12.10, 13.1