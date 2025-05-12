"""
Write a function to extract all the adjacent coordinates of the given coordinate tuple.
assert get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
"""

def get_coordinates(coordinate):
    """
    This function takes a coordinate tuple as input and returns a list of all the adjacent coordinates.
    """
    adjacent_coordinates = []
    x, y = coordinate
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 10 and 0 <= new_y < 10:
            adjacent_coordinates.append((new_x, new_y))
    return adjacent_coordinates

# Test the function
print(get_coordinates((3, 4)))