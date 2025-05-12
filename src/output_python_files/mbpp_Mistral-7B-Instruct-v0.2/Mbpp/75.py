"""
Write a function to find tuples which have all elements divisible by k from the given list of tuples.
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
"""
def find_tuples(tuples_list, k):
    """
    :param tuples_list: list of tuples
    :param k: integer
    :return: list of tuples which have all elements divisible by k
    """
    result = []
    for tuple in tuples_list:
        if all(x % k == 0 for x in tuple):
            result.append(tuple)
    return result

# Test the function
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
assert find_tuples([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 2) == []
assert find_tuples([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 3) == []
assert find_tuples([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 1) == [(1, 2, 3), (4, 5, 6), (7, 8, 9)]