"""
Write a function to convert the given tuple to a key-value dictionary using adjacent elements. https://www.geeksforgeeks.org/python-convert-tuple-to-adjacent-pair-dictionary/
assert tuple_to_dict((1, 5, 7, 10, 13, 5)) == {1: 5, 7: 10, 13: 5}
"""
def tuple_to_dict(t):
    """
    :param t: tuple
    :return: dict
    """
    d = {}
    for i in range(len(t) - 1):
        d[t[i]] = t[i+1]
    return d

if __name__ == "__main__":
    assert tuple_to_dict((1, 5, 7, 10, 13, 5)) == {1: 5, 7: 10, 13: 5}
    assert tuple_to_dict((1, 2, 3, 4, 5)) == {1: 2, 3: 4}
    assert tuple_to_dict((1, 2, 3)) == {1: 2}
    assert tuple_to_dict((1,)) == {}
    assert tuple_to_dict(()) == {}
    assert tuple_to_dict((1)) == {1: None}
    assert tuple_to_dict((1, 1, 1)) == {1: 1}
    assert tuple_to_dict((1, 1, 1, 1)) == {1: 1}
    assert tuple_to_dict((1, 1, 1, 1, 1)) == {1: 1}
    assert tuple_to_dict((1, 1, 1, 1, 1, 1)) == {1: 1}
    assert tuple_to_dict((1, 1, 1, 1, 1, 1, 1)) == {1: 1}
    assert tuple_to_dict((1, 1, 1, 1, 1, 1, 1, 1)) == {1: 1}
    assert tuple_to_dict((1, 1, 1, 1, 1, 1, 1, 1, 1)) == {1: 1}
    assert tuple_to_dict((1, 1, 1, 1, 1, 1, 1, 1, 1, 1)) == {1: 1}
    assert tuple_to_dict((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)) == {1: 1}
    assert tuple_to_dict((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)) == {1: 1}
    assert tuple_to_dict((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)) == {1: 1}
    assert tuple_to_dict((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)) == {1: 1}
    assert tuple_to_dict((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)) == {1: 1}
    assert tuple_to_dict((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)) == {1: 1}
    assert tuple_to_dict((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)) == {1: 1}
    assert tuple_to_dict((1, 1, 1, 1