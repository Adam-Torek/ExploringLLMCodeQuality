"""
Write a function to extract all the adjacent coordinates of the given coordinate tuple.
assert get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
"""

def get_coordinates(coordinate):
    """
    :param coordinate: tuple of two integers
    :return: list of tuples of adjacent coordinates
    """
    x, y = coordinate
    result = []
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < 10 and 0 <= ny < 10:
            result.append((nx, ny))
    return result