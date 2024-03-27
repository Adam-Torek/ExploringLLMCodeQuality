"""
Write a function to count bidirectional tuple pairs.
assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
"""
def count_bidirectional(tuples):
    """
    :param tuples: list of tuples
    :return: int
    """
    bidirectional_pairs = set()
    for pair in tuples:
        if pair in tuples and pair[::-1] in tuples:
            bidirectional_pairs.add(pair)
    return len(bidirectional_pairs)

assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)]) == 3
assert count_bidirectional([(1, 2), (2, 1)]) == 1
assert count_bidirectional([]) == 0
assert count_bidirectional([(1, 2)]) == 0
assert count_bidirectional([(1, 1)]) == 0
assert count_bidirectional([(1, 1), (1, 1)]) == 1
assert count_bidirectional([(1, 1), (1, 1), (1, 1)]) == 1
assert count_bidirectional([(1, 1), (1, 1), (1, 1), (1, 1)]) == 2
assert count_bidirectional([(1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]) == 3
assert count_bidirectional([(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]) == 4
assert count_bidirectional([(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]) == 5
assert count_bidirectional([(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]) == 6
assert count_bidirectional([(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]) == 7
assert count_bidirectional([(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]) == 8
assert count_bidirectional([(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]) == 9
assert count_bidirectional([(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]) == 10
assert count_bidirectional([(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]) == 11
assert count_bidirectional([(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (