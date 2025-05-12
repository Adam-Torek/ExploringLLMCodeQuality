"""
Write a function to find the n'th star number.
assert find_star_num(3) == 37
"""

def find_star_num(n):
    """
    :param n: int
    :return: int
    """
    if n < 1:
        return 0
    else:
        return sum([1] + [2**i for i in range(1, n)])


if __name__ == '__main__':
    assert find_star_num(3) == 37