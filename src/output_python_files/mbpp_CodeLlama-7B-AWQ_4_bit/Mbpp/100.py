"""
Write a function to find the next smallest palindrome of a specified integer, returned as an integer.
assert next_smallest_palindrome(99)==101
"""


def next_smallest_palindrome(n):
    """
    :param n: int
    :return: int
    """
    if n < 10:
        return n
    if n % 10 == 0:
        return n + 1
    if n % 10 == 1:
        return n + 10
    if n % 10 == 5:
        return n + 10
    if n % 10 == 9:
        return n + 10
    if n % 10 == 7:
        return n + 10
    if n % 10 == 3:
        return n + 10
    if n % 10 == 8:
        return n + 10
    if n % 10 == 4:
        return n + 10
    if n % 10 == 6:
        return n + 10
    if n % 10 == 2:
        return n + 10
    if n % 10 ==