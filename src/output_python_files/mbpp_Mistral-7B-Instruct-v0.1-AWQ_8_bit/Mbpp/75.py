"""
Write a function to find tuples which have all elements divisible by k from the given list of tuples.
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
"""

def find_tuples(tuples, k):
    """
    :param tuples: list of tuples
    :param k: integer
    :return: list of tuples
    """
    result = []
    for tuple in tuples:
        if all(x % k == 0 for x in tuple):
            result.append(tuple)
    return result