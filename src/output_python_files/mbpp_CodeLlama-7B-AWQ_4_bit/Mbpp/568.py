"""
Write a function to create a list of N empty dictionaries.
assert empty_list(5)==[{},{},{},{},{}]
"""


def empty_list(n):
    """
    Create a list of N empty dictionaries.
    :param n: int
    :return: list
    """
    return [{} for _ in range(n)]


if __name__ == '__main__':
    print(empty_list(5))