"""
Write a function to find the tuple intersection of elements in the given tuple list irrespective of their order.
assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)] , [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
"""
from collections import defaultdict

def tuple_intersection(*args):
    """
    Function to find the tuple intersection of elements in the given tuple list irrespective of their order.
    :param args: list of tuples
    :return: set of common elements
    """
    d = defaultdict(int)
    for tpl in args[0]:
        for elem in tpl:
            d[elem] += 1

    result = set()
    for tpl in args[1:]:
        for elem in tpl:
            if d[elem] > 0:
                result.add(elem)
                d[elem] -= 1

    return result

if __name__ == "__main__":
    assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)], [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
    assert tuple_intersection([(1, 2), (3, 4), (5, 6), (7, 8)], [(1, 2), (3, 4), (5, 6), (9, 11)]) == {(1, 2), (3, 4), (5, 6)}
    assert tuple_intersection([(1, 2), (3, 4), (5, 6), (7, 8)], [(1, 2), (3, 4), (5, 6), (9, 11), (1, 3)]) == {(1, 2), (3, 4), (5, 6)}
    assert tuple_intersection([], []) == set()
    assert tuple_intersection([], [(1, 2)]) == set()
    assert tuple_intersection([(1, 2)], []) == set()
    assert tuple_intersection([(1, 2)], [(1, 2)]) == {(1, 2)}
    assert tuple_intersection([(1, 2), (1, 2)], [(1, 2), (1, 2)]) == {(1, 2)}
    assert tuple_intersection([(1, 2), (1, 2)], [(1, 3), (1, 2)]) == {(1, 2)}
    assert tuple_intersection([(1, 2), (1, 2)], [(1, 3), (1, 2), (1, 2)]) == {(1, 2)}
    assert tuple_intersection([(1, 2), (1, 2)], [(1, 3), (1, 2), (1, 2), (1, 2)]) == {(1, 2)}
    assert tuple_intersection([(1, 2), (1, 2)], [(1, 3), (1, 2), (1, 2), (1, 2), (1, 2)]) == {(1, 2)}
    assert tuple_intersection([(1, 2), (1, 2)], [(1, 3), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2)]) == {(1, 2)}
    assert tuple_intersection([(1, 2), (1, 2)], [(1, 3), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2)]) == {(1, 2)}
    assert tuple_intersection([(1, 2), (1, 2)], [(