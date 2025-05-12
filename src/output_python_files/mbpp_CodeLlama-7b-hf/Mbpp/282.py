"""
Write a function to subtract two lists element-wise.
assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
"""

def sub_list(list1, list2):
    """
    Subtracts two lists element-wise.
    """
    if len(list1) != len(list2):
        raise ValueError("Lists must be of equal length")
    else:
        return [x - y for x, y in zip(list1, list2)]


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # print(sub_list([1, 2, 3], [4, 5, 6]))
    # print(sub_list([1, 2, 3], [4, 5, 6, 7]))
    # print(sub_list([1, 2, 3], [4, 5, 6, 7, 8]))
    # print(sub_list([1, 2, 3], [4, 5, 6, 7, 8, 9]))
    # print(sub_list([1, 2, 3], [4, 5, 6, 7, 8, 9, 10]))
    # print(sub_list([1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11]))
    # print(sub_list([1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11, 12]))
    # print(sub_list([1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
    # print(sub_list([1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
    # print(sub_list([1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    # print(sub_list([1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
    # print(sub_list([1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))
    # print(sub_list([1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))
    # print(sub_list([1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
    # print(sub_list([1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    # print(sub_list([1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11,