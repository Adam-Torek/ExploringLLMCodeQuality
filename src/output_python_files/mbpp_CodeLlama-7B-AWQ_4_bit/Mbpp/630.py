"""
Write a function to extract all the adjacent coordinates of the given coordinate tuple.
assert get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
"""


def get_coordinates(coordinates):
    """
    >>> get_coordinates((3, 4))
    [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
    """
    return [
        [coordinates[0] - 1, coordinates[1] - 1],
        [coordinates[0] - 1, coordinates[1]],
        [coordinates[0] - 1, coordinates[1] + 1],
        [coordinates[0], coordinates[1] - 1],
        [coordinates[0], coordinates[1]],
        [coordinates[0], coordinates[1] + 1],
        [coordinates[0] + 1, coordinates[1] - 1],
        [coordinates[0] + 1, coordinates[1]],
        [coordinates[0] + 1, coordinates[1] + 1],
    ]


if __name__ == "__main__":
    import doctest

    doctest.testmod()