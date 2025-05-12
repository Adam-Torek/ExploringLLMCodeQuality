"""
Write a function to count bidirectional tuple pairs.
assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
"""
def count_bidirectional(tuples):
    """
    Count bidirectional tuple pairs in a given list of tuples.
    """
    bidirectional_pairs = set()
    for pair in tuples:
        if pair in bidirectional_pairs:
            continue
        if pair[::-1] in bidirectional_pairs:
            bidirectional_pairs.add(pair)
            continue
        if len(pair) != 2:
            raise ValueError("Each tuple in the list should have exactly 2 elements.")
        bidirectional_pairs.add(pair)
    return len(bidirectional_pairs)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)]) == 3
    assert count_bidirectional([(1, 2), (2, 1)]) == 1
    assert count_bidirectional([]) == 0
    assert count_bidirectional([(1, 2)]) == 0
    assert count_bidirectional([(1, 1)]) == 0
    assert count_bidirectional([(1, 2), (2, 1), (1, 1)]) == 1
    assert count_bidirectional([(1, 2), (2, 1), (1, 1), (1, 2)]) == 2
    assert count_bidirectional([(1, 2), (2, 1), (1, 1), (1, 2), (2, 1)]) == 2
    assert count_bidirectional([(1, 2), (2, 1), (1, 1), (1, 2), (2, 1), (1, 2)]) == 3
    assert count_bidirectional([(1, 2), (2, 1), (1, 1), (1, 2), (2, 1), (1, 2), (1, 2)]) == 3
    assert count_bidirectional([(1, 2), (2, 1), (1, 1), (1, 2), (2, 1), (1, 2), (1, 2), (1, 2)]) == 4
    assert count_bidirectional([(1, 2), (2, 1), (1, 1), (1, 2), (2, 1), (1, 2), (1, 2), (1, 2), (1, 2)]) == 5
    assert count_bidirectional([(1, 2), (2, 1), (1, 1), (1, 2), (2, 1), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2)]) == 6
    assert count_bidirectional([(1, 2), (2, 1), (1, 1), (1, 2), (2, 1), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2)]) == 7
    assert count_bidirectional([(1, 2), (2, 1), (1, 1), (1, 2), (2, 1), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2)]) == 8
    assert count_bidirectional([(1, 2), (2, 1), (1, 1), (1, 2), (2, 1), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (