"""
Write a function to extract the number of unique tuples in the given list.
assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)] ) == 3
"""
def extract_freq(lst):
    """
    :param lst: list of tuples
    :return: number of unique tuples in the given list
    """
    return len(set(lst))

assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)]) == 3