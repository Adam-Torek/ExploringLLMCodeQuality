"""
Write a function to find the union of the elements of two given tuples and output them in sorted order.
assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)
"""

def union_elements(t1, t2):
    """
    :param t1: tuple
    :param t2: tuple
    :return: tuple
    """
    return tuple(sorted(set(t1 + t2)))


if __name__ == '__main__':
    print(union_elements((3, 4, 5, 6), (5, 7, 4, 10)))
    print(union_elements((3, 4, 5, 6), (5, 7, 4, 10, 3)))
    print(union_elements((3, 4, 5, 6), (5, 7, 4, 10, 3, 3)))
    print(union_elements((3, 4, 5, 6), (5, 7, 4, 10, 3, 3, 3)))
    print(union_elements((3, 4, 5, 6), (5, 7, 4, 10, 3, 3, 3, 3)))
    print(union_elements((3, 4, 5, 6), (5, 7, 4, 10, 3, 3, 3, 3, 3)))
    print(union_elements((3, 4, 5, 6), (5, 7, 4, 10, 3, 3, 3, 3, 3, 3)))
    print(union_elements((3, 4, 5, 6), (5, 7, 4, 10, 3, 3, 3, 3, 3, 3, 3)))
    print(union_elements((3, 4, 5, 6), (5, 7, 4, 10, 3, 3, 3, 3, 3, 3, 3, 3)))
    print(union_elements((3, 4, 5, 6), (5, 7, 4, 10, 3, 3, 3, 3, 3, 3, 3, 3, 3)))
    print(union_elements((3, 4, 5, 6), (5, 7, 4, 10, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3)))
    print(union_elements((3, 4, 5, 6), (5, 7, 4, 10, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3)))
    print(union_elements((3, 4, 5, 6), (5, 7, 4, 10, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3)))
    print(union_elements((3, 4, 5, 6), (5, 7, 4, 10, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3)))
    print(union_elements((3, 4, 5, 6), (5, 7, 4, 10, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3)))
    print(union_elements((3, 4, 5, 6), (5, 7, 4, 10, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3)))
    print(union