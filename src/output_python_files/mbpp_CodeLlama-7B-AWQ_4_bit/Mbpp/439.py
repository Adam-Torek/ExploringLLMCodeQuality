"""
Write a function to join a list of multiple integers into a single integer.
assert multiple_to_single([11, 33, 50])==113350
"""


def multiple_to_single(lst):
    """
    :param lst: list of integers
    :return: integer
    """
    return int(''.join(map(str, lst)))


if __name__ == '__main__':
    print(multiple_to_single([11, 33, 50]))
    print(multiple_to_single([11, 33, 50, 22, 44, 66, 88, 99]))
    print(multiple_to_single([11, 33, 50, 22, 44, 66, 88, 99, 100]))
    print(multiple_to_single([11, 33, 50, 22, 44, 66, 88, 99, 100, 101]))
    print(multiple_to_single([11, 33, 50, 22, 44, 66, 88, 99, 100, 101, 102]))
    print(multiple_to_single([11, 33, 50, 22, 44, 66, 88, 99, 100, 101, 102, 103]))
    print(multiple_to_single([11, 33, 50, 22, 44, 66, 88, 99, 100, 101, 102, 103, 104]))
    print(multiple_to_single([11, 33, 50, 22, 44, 66, 88, 99, 100, 101, 102, 103, 104, 105]))
    print(multiple_to_single([11, 33, 50, 22, 44, 66, 88, 99, 100, 101, 102, 103, 104, 105, 106]))
    print(multiple_to_single([11, 33, 50, 22, 44, 66, 88, 99, 100, 101, 102, 103, 104, 105, 106, 107]))
    print(multiple_to_single([11, 33, 50, 22, 44, 66, 88, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108]))
    print(multiple_to_single([11, 33, 50, 22, 44, 66, 88, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109]))
    print(multiple_to_single([11, 33, 50, 22, 44, 66, 88, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]))
    print(multiple_to_single([11, 33, 50, 22, 44, 66, 88, 99, 100, 101, 102,