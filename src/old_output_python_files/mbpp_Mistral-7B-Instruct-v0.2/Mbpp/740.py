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
    assert tuple_to_dict((1, 5, 7, 10, 13, 5, 11, 15)) == {1: 5, 7: 10, 13: 5, 11: 15}
    assert tuple_to_dict((1, 5, 7, 10, 13, 5, 11, 15, 17)) == {1: 5, 7: 10, 13: 5, 11: 15, 17: None}
    assert tuple_to_dict((1, 5, 7, 10, 13, 5, 11, 15, 17, 19)) == {1: 5, 7: 10, 13: 5, 11: 15, 17: 19}
    assert tuple_to_dict((1, 5, 7, 10, 13, 5, 11, 15, 17, 19, 21)) == {1: 5, 7: 10, 13: 5, 11: 15, 17: 19, 19: 21}
    assert tuple_to_dict((1, 5, 7, 10, 13, 5, 11, 15, 17, 19, 21, 23)) == {1: 5, 7: 10, 13: 5, 11: 15, 17: 19, 19: 21, 21: 23}
    assert tuple_to_dict((1, 5, 7, 10, 13, 5, 11, 15, 17, 19, 21, 23, 25)) == {1: 5, 7: 10, 13: 5, 11: 15, 17: 19, 19: 21, 21: 23, 23: 25}
    assert tuple_to_dict((1, 5, 7, 10, 13, 5, 11, 15, 17, 19, 21, 23, 25, 27)) == {1: 5, 7: 10, 13: 5, 11: 15, 17: 19, 19: 21, 21: 23, 23: 25, 25: 27}
    assert tuple_to_dict((1, 5, 7, 10, 13, 5, 11, 15, 17, 19, 21, 23, 25, 27, 29)) == {1: 5, 7: 10, 13: 5, 11: 15, 17: 19, 19: 21, 21: 23, 23: 25, 25: 27