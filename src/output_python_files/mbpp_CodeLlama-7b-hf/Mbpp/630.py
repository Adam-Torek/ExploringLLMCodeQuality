"""
Write a function to extract all the adjacent coordinates of the given coordinate tuple.
assert get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
"""


def get_coordinates(coord):
    """
    :param coord: tuple of ints
    :return: list of tuples
    """
    x, y = coord
    return [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y), (x, y + 1), (x + 1, y - 1), (x + 1, y),
            (x + 1, y + 1)]


if __name__ == '__main__':
    print(get_coordinates((3, 4)))
    print(get_coordinates((1, 1)))
    print(get_coordinates((1, 2)))
    print(get_coordinates((2, 1)))
    print(get_coordinates((2, 2)))
    print(get_coordinates((3, 1)))
    print(get_coordinates((3, 2)))
    print(get_coordinates((4, 1)))
    print(get_coordinates((4, 2)))
    print(get_coordinates((1, 3)))
    print(get_coordinates((2, 3)))
    print(get_coordinates((3, 3)))
    print(get_coordinates((4, 3)))
    print(get_coordinates((1, 4)))
    print(get_coordinates((2, 4)))
    print(get_coordinates((3, 4)))
    print(get_coordinates((4, 4)))
    print(get_coordinates((1, 5)))
    print(get_coordinates((2, 5)))
    print(get_coordinates((3, 5)))
    print(get_coordinates((4, 5)))
    print(get_coordinates((5, 1)))
    print(get_coordinates((5, 2)))
    print(get_coordinates((5, 3)))
    print(get_coordinates((5, 4)))
    print(get_coordinates((5, 5)))
    print(get_coordinates((6, 1)))
    print(get_coordinates((6, 2)))
    print(get_coordinates((6, 3)))
    print(get_coordinates((6, 4)))
    print(get_coordinates((6, 5)))
    print(get_coordinates((6, 6)))
    print(get_coordinates((7, 1)))
    print(get_coordinates((7, 2)))
    print(get_coordinates((7, 3)))
    print(get_coordinates((7, 4)))
    print(get_coordinates((7, 5)))
    print(get_coordinates((7, 6)))
    print(get_coordinates((7, 7)))
    print(get_coordinates((8, 1)))
    print(get_coordinates((8, 2)))
    print(get_coordinates((8, 3)))
    print(get_coordinates((8, 4)))
    print(get_coordinates((8, 5)))
    print(get_coordinates((8, 6)))
    print(get_coordinates((8, 7)))
    print(get_coordinates((8, 8)))
    print(get_coordinates((9, 1)))
    print(get_coordinates((9, 2)))
    print(get_coordinates((9, 3)))
    print(get_coordinates((9, 4)))
    print(get_coordinates((9, 5)))
    print(get_coordinates((9, 6)))
    print(get_coordinates((9, 7)))
    print(get_coordinates((9, 8)))
    print(get_coordinates((9, 9)))
    print(get_coordinates((