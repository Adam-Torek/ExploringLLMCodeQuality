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
        return sum([(x + 1) * x for x in range(1, n)])