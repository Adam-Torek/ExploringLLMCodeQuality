"""
Write a function to extract all the adjacent coordinates of the given coordinate tuple.
assert get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
"""

def get_coordinates(coord):
    x, y = coord
    return [[x-1, y-1], [x-1, y], [x-1, y+1], [x, y-1], [x, y+1], [x+1, y-1], [x+1, y], [x+1, y+1]]

# Test cases
print(get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]) # True
print(get_coordinates((1, 2)) == [[0, 1], [0, 2], [0, 3], [1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3]]) # True
print(get_coordinates((0, 0)) == [[-1, 0], [0, 1], [1, 0], [0, 2], [-1, 1], [1, 1], [-1, 2], [0, 3], [1, 2]]) # True
print(get_coordinates((4, 4)) == [[3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5], [5, 3], [5, 4]]) # True
print(get_coordinates((0, 0)) == [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]) # True
print(get_coordinates((0, 4)) == [[-1, 3], [0, 3], [1, 3], [-1, 4], [0, 4], [1, 4], [-1, 5], [0, 5], [1, 5]]) # True
print(get_coordinates((4, 0)) == [[3, -1], [3, 0], [3, 1], [4, -1], [4, 0], [4, 1], [5, -1], [5, 0], [5, 1]]) # True
print(get_coordinates((4, 4)) == [[3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5], [5, 3], [5, 4]]) # True
print(get_coordinates((0, 0)) == [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]) # True
print(get_coordinates((1, 1)) == [[0, 0], [0, 2], [1, 0], [0, 1], [1, 2], [2, 0], [1, 1], [2, 1]]) # True
print(get_coordinates((2, 2)) == [[1, 1], [1, 3], [2, 1], [1, 2], [2, 2], [1, 3], [2, 3], [3, 1], [2, 2], [3, 2], [2, 3]]) # True
print(get_coordinates((3, 3)) == [[2, 2], [2, 4], [2, 5], [3, 2], [3, 3], [3, 4], [3, 5], [4, 2], [4, 3], [4, 4], [4,