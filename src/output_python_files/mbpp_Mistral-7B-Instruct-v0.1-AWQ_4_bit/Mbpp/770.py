"""
Write a python function to find the sum of fourth power of first n odd natural numbers.
assert odd_num_sum(2) == 82
"""

def odd_num_sum(n):
    """
    :param n: int
    :return: int
    """
    return sum(i**4 for i in range(1, n+1, 2))


if __name__ == '__main__':
    assert odd_num_sum(2) == 82