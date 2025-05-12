"""
Write a function to find the maximum difference between available pairs in the given tuple list.
assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
"""

def max_difference(tuples):
    """
    :param tuples: list of tuples
    :return: int
    """
    return max(abs(x[0] - x[1]) for x in tuples)

if __name__ == "__main__":
    assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
    assert max_difference([(1, 2), (3, 4), (5, 6), (7, 8)]) == 7
    assert max_difference([(1, 1), (1, 1), (1, 1), (1, 1)]) == 0
    assert max_difference([]) == 0
    assert max_difference([(1, 1)]) == 0