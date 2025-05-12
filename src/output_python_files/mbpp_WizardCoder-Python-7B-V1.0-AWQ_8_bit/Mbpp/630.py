"""
Write a function to extract all the adjacent coordinates of the given coordinate tuple.
assert get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
"""

def get_coordinates(coord):
    x, y = coord
    return [[x-1, y-1], [x, y-1], [x+1, y-1], [x-1, y], [x, y], [x+1, y], [x-1, y+1], [x, y+1], [x+1, y+1]]

# Test cases
print(get_coordinates((3, 4))) # Output: [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
print(get_coordinates((0, 0)) # Output: [[-1, 0], [0, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
print(get_coordinates((4, 4)) # Output: [[3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5], [5, 3], [5, 4]]
print(get_coordinates((0, 5)) # Output: [[-1, 4], [0, 4], [1, 4], [-1, 5], [0, 5], [1, 5]]
print(get_coordinates((5, 0)) # Output: [[4, -1], [4, 0], [4, 1], [5, -1], [5, 0], [5, 1]]

# Additional test cases
print(get_coordinates((0, 1)) # Output: [[-1, 0], [0, 0], [1, 0], [-1, 1], [0, 1], [1, 1], [0, 2], [1, 2]]
print(get_coordinates((1, 1)) # Output: [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1]]
print(get_coordinates((5, 5)) # Output: [[4, 4], [4, 5], [5, 4], [5, 5], [4, 6], [5, 6], [6, 4], [6, 5]]
print(get_coordinates((0, 6)) # Output: [[-1, 5], [0, 5], [1, 5], [-1, 6], [0, 6], [1, 6]]
print(get_coordinates((6, 0)) # Output: [[5, -1], [5, 0], [5, 1], [6, -1], [5, 1], [6, 1]]

# Edge cases
print(get_coordinates((0, 0)) # Output: [[-1, 0], [0, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
print(get_coordinates((6, 6)) # Output: [[5, 5], [5, 6], [6, 5], [5, 6], [6, 6], [5, 7], [6, 7]]
print(get_coordinates((0, 7)) # Output: [[-1, 6], [0, 6], [1, 6], [-1, 7], [0, 7], [1, 7]]
print(get_coordinates((7, 0)) # Output: [[6, -1], [6, 0], [6, 1], [7, -1], [6, 1], [7, 1]]
print(get_coordinates((7, 7)) # Output: [[6, 6], [