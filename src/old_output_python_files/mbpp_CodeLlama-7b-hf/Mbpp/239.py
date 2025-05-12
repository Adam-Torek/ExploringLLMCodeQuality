"""
Write a function that takes in positive integers m and n and finds the number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.
assert get_total_number_of_sequences(10, 4) == 4
"""


def get_total_number_of_sequences(m, n):
    """
    >>> get_total_number_of_sequences(10, 4)
    4
    >>> get_total_number_of_sequences(10, 3)
    3
    >>> get_total_number_of_sequences(10, 2)
    2
    >>> get_total_number_of_sequences(10, 1)
    1
    >>> get_total_number_of_sequences(10, 0)
    1
    >>> get_total_number_of_sequences(10, 10)
    1
    >>> get_total_number_of_sequences(10, 11)
    0
    >>> get_total_number_of_sequences(10, 12)
    0
    >>> get_total_number_of_sequences(10, 13)
    0
    >>> get_total_number_of_sequences(10, 14)
    0
    >>> get_total_number_of_sequences(10, 15)
    0
    >>> get_total_number_of_sequences(10, 16)
    0
    >>> get_total_number_of_sequences(10, 17)
    0
    >>> get_total_number_of_sequences(10, 18)
    0
    >>> get_total_number_of_sequences(10, 19)
    0
    >>> get_total_number_of_sequences(10, 20)
    0
    >>> get_total_number_of_sequences(10, 21)
    0
    >>> get_total_number_of_sequences(10, 22)
    0
    >>> get_total_number_of_sequences(10, 23)
    0
    >>> get_total_number_of_sequences(10, 24)
    0
    >>> get_total_number_of_sequences(10, 25)
    0
    >>> get_total_number_of_sequences(10, 26)
    0
    >>> get_total_number_of_sequences(10, 27)
    0
    >>> get_total_number_of_sequences(10, 28)
    0
    >>> get_total_number_of_sequences(10, 29)
    0
    >>> get_total_number_of_sequences(10, 30)
    0
    >>> get_total_number_of_sequences(10, 31)
    0
    >>> get_total_number_of_sequences(10, 32)
    0
    >>> get_total_number_of_sequences(10, 33)
    0
    >>> get_total_number_of_sequences(10, 34)
    0
    >>> get_total_number_of_sequences(10, 35)
    0
    >>> get_total_number_of_sequences(10, 36)
    0
    >>> get_total_number_of_sequences(10, 37)
    0
    >>> get_total_number_of_sequences(10, 38)
    0
    >>> get_total_number_of_sequences(10, 39)
    0
    >>> get_total_number_of_sequences(10, 40)
    0
    >>> get_total_number_of_sequences(10, 41)
    0
    >>> get_total_number_of_sequences(10, 42)
    0
    >>> get_total_number_of_sequences(10,