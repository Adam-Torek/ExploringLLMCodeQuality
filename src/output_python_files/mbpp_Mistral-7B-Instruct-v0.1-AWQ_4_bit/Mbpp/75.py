"""
Write a function to find tuples which have all elements divisible by k from the given list of tuples.
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
"""

def find_tuples(lst, k):
    """
    :param lst: list of tuples
    :param k: integer
    :return: list of tuples where all elements are divisible by k
    """
    return [tuple(x for x in tpl if x % k == 0) for tpl in lst]


if __name__ == '__main__':
    print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6))