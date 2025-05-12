"""
Write a function to convert tuple string to integer tuple.
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
"""

def tuple_str_int(s):
    return tuple(map(int, s.strip('()').split(', '))

# Test cases
print(tuple_str_int("(7, 8, 9)")) # Output: (7, 8, 9)
print(tuple_str_int("(1, 2, 3, 4, 5)")) # Output: (1, 2, 3, 4, 5)
print(tuple_str_int("(10, 20, 30, 40, 50, 60)")) # Output: (10, 20, 30, 40, 50, 60)
print(tuple_str_int("(100, 200, 300, 400, 500, 600, 700, 800, 900)")) # Output: (100, 200, 300, 400, 500, 600, 700, 800, 900)
print(tuple_str_int("(1000, 200, 300, 400, 500, 600, 700, 800, 900, 10000, 11000, 1200, 1300, 1400, 1500)")) # Output: (100, 200, 300, 400, 500, 600, 700, 800, 900, 10000, 11000, 1200, 1300, 1400, 1500)

# Edge cases
print(tuple_str_int("(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)") == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) # Output: True
print(tuple_str_int("(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)") == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) # Output: True
print(tuple_str_int("(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)") == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) # Output: True
print(tuple_str_int("(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)") == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) # Output: True
print(tuple_str_int("(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)") == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) # Output: True
print(tuple_str_int("(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)") == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) # Output: True
print(tuple_str_int("(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)") == (1, 2, 3, 4, 5, 6, 7, 8,