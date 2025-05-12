"""
Write a function to return a list of all pairs of consecutive items in a given list.
assert pair_wise([1,1,2,3,3,4,4,5])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
"""
def pair_wise(input_list):
    """
    :param input_list: list of integers
    :return: list of tuples representing pairs of consecutive integers
    """
    if len(input_list) < 2:
        return []
    return list(zip(input_list, input_list[1:]))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    assert pair_wise([1,1,2,3,3,4,4,5])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
    assert pair_wise([])==[]
    assert pair_wise([1])==[]
    assert pair_wise([1,1])==[(1, 1)]
    assert pair_wise([1,2])==[(1, 2)]
    assert pair_wise([1,1,2,3])==[(1, 1), (1, 2), (2, 3)]
    assert pair_wise([1,1,2,3,3,4,4,5,6])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5), (5, 6)]