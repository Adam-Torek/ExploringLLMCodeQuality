"""
Write a function to find the tuple intersection of elements in the given tuple list irrespective of their order.
assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)] , [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
"""
from collections import defaultdict

def tuple_intersection(*args):
    """
    Function to find the tuple intersection of elements in the given tuple list irrespective of their order.
    :param args: list of tuples
    :return: set of common elements in all tuples
    """
    d = defaultdict(int)
    for tpl in args:
        for elem in tpl:
            d[elem] += 1

    return {elem: val for elem, val in d.items() if val == len(args)}

if __name__ == "__main__":
    assert tuple_intersection((3, 4), (5, 6), (9, 10), (4, 5)) == {(4, 5), (3, 4), (5, 6)}
    assert tuple_intersection((5, 4), (3, 4), (6, 5), (9, 11)) == set()
    assert tuple_intersection((1, 2, 3), (2, 3, 4), (3, 4, 5)) == {(2, 3), (3, 4)}
    assert tuple_intersection((1, 2, 3), (2, 3, 4), (3, 4, 5), (3, 4, 5)) == {(3, 4)}
    assert tuple_intersection() == set()