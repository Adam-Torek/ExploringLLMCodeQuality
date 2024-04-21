"""
Write a function to extract the number of unique tuples in the given list.
assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)] ) == 3
"""


def extract_freq(tuples):
    """
    :param tuples: list of tuples
    :return: number of unique tuples
    """
    return len(set(tuples))


if __name__ == '__main__':
    print(extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)]))
    print(extract_freq([(3, 4), (1, 2), (4, 3), (5, 6), (3, 4), (1, 2), (4, 3), (5, 6)]))
    print(extract_freq([(3, 4), (1, 2), (4, 3), (5, 6), (3, 4), (1, 2), (4, 3), (5, 6), (3, 4), (1, 2), (4, 3), (5, 6)]))
    print(extract_freq([(3, 4), (1, 2), (4, 3), (5, 6), (3, 4), (1, 2), (4, 3), (5, 6), (3, 4), (1, 2), (4, 3), (5, 6), (3, 4), (1, 2), (4, 3), (5, 6)]))
    print(extract_freq([(3, 4), (1, 2), (4, 3), (5, 6), (3, 4), (1, 2), (4, 3), (5, 6), (3, 4), (1, 2), (4, 3), (5, 6), (3, 4), (1, 2), (4, 3), (5, 6), (3, 4), (1, 2), (4, 3), (5, 6)]))
    print(extract_freq([(3, 4), (1, 2), (4, 3), (5, 6), (3, 4), (1, 2), (4, 3), (5, 6), (3, 4), (1, 2), (4, 3), (5, 6), (3, 4), (1, 2), (4, 3), (5, 6), (3, 4), (1, 2), (4, 3), (5, 6), (3, 4), (1, 2), (4, 3), (5, 6), (3, 4), (1, 2), (4, 3), (5, 6), (3, 4), (1, 2), (4, 3), (5, 6), (3, 4), (1, 2), (4, 3), (5, 6), (3, 4), (1, 2), (4, 3), (5, 6), (3, 4), (1, 2), (4, 3), (5, 6), (3, 4), (1, 2), (4, 3), (5, 6), (3, 4), (1, 2), (4, 3), (5, 6), (3, 4), (1, 2), (4, 3), (5, 6), (3, 4), (1, 2), (4, 3), (5, 6), (3, 4), (1, 2), (4, 3), (5, 6), (3, 4), (1, 2), (4, 3), (5, 6), (3, 4), (1, 2), (4, 3), (5, 6), (3, 4), (1, 2), (4, 3), (5, 6), (3, 4), (1, 2), (4, 3), (5, 6), (3, 4),