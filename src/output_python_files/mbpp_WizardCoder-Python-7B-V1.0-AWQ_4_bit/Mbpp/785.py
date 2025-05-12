"""
Write a function to convert tuple string to integer tuple.
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
"""

def tuple_str_int(string):
    return tuple(map(int, string.strip('()').split(', '))

# Test cases
print(tuple_str_int("(7, 8, 9)")) # Output: (7, 8, 9)
print(tuple_str_int("(1, 2, 3, 4, 5)")) # Output: (1, 2, 3, 4, 5)
print(tuple_str_int("(10, 20, 30, 40, 50, 60, 70)")) # Output: (10, 20, 30, 40, 50, 60, 70)
print(tuple_str_int("(100, 200, 300, 400, 500, 600, 700, 800, 900, 1000)")) # Output: (100, 200, 300, 400, 500, 600, 700, 800, 900, 100)