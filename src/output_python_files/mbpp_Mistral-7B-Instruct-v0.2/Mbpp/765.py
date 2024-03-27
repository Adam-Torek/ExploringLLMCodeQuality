"""
Write a function to find nth polite number. geeksforgeeks.org/n-th-polite-number/
assert is_polite(7) == 11
"""

import math


def is_polite(n):
    """
    :param n: int
    :return: bool
    """
    if n < 1:
        return False

    n_str = str(n)
    n_len = len(n_str)

    if n_len % 2 == 1:
        return False

    n_str_len = len(n_str) // 2

    for i in range(n_str_len):
        if int(n_str[i]) > int(n_str[n_str_len + i]):
            return False

    return True


def nth_polite_number(n):
    """
    :param n: int
    :return: int
    """
    polite_number = 0
    current_number = 1

    while True:
        if is_polite(current_number):
            polite_number = current_number
            if n - 1 < polite_number:
                n -= 1
            else:
                return polite_number

        current_number += 1


if __name__ == "__main__":
    n = 10
    print(nth_polite_number(n))</s>