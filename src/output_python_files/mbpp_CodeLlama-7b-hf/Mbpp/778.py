"""
Write a function to pack consecutive duplicates of a given list elements into sublists.
assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
"""


def pack_consecutive_duplicates(lst):
    """
    >>> pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])
    [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
    """
    if not lst:
        return []
    result = []
    current = []
    for i in lst:
        if current and i == current[-1]:
            current.append(i)
        else:
            if current:
                result.append(current)
            current = [i]
    if current:
        result.append(current)
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()