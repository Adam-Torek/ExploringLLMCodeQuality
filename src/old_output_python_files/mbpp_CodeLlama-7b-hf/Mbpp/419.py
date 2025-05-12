"""
Write a function to round every number of a given list of numbers and print the total sum multiplied by the length of the list.
assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])==243
"""


def round_and_sum(numbers):
    """
    :param numbers: list of numbers
    :return: sum of rounded numbers multiplied by the length of the list
    """
    return sum(round(number) for number in numbers) * len(numbers)


if __name__ == '__main__':
    print(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]))
    print(round_and_sum([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.10]))
    print(round_and_sum([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.10, 11.11, 12.12, 13.13, 14.14, 15.15, 16.16, 17.17, 18.18, 19.19, 20.20]))
    print(round_and_sum([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.10, 11.11, 12.12, 13.13, 14.14, 15.15, 16.16, 17.17, 18.18, 19.19, 20.20, 21.21, 22.22, 23.23, 24.24, 25.25, 26.26, 27.27, 28.28, 29.29, 30.30]))
    print(round_and_sum([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.10, 11.11, 12.12, 13.13, 14.14, 15.15, 16.16, 17.17, 18.18, 19.19, 20.20, 21.21, 22.22, 23.23, 24.24, 25.25, 26.26, 27.27, 28.28, 29.29, 30.30, 31.31, 32.32, 33.33, 34.34, 35.35, 36.36, 37.37, 38.38, 39.39, 40.40, 41.41, 42.42, 43.43, 44.44, 45.45, 46.46, 47.47, 48.48, 49.49, 50.50, 51.51, 52.52, 53.53, 54.54, 55.55, 56.56, 57