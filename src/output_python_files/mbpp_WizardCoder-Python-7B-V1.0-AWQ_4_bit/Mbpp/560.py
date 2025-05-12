"""
Write a function to find the union of the elements of two given tuples and output them in sorted order.
assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)
"""

def union_elements(tup1, tup2):
    """
    Find the union of the elements of two given tuples and output them in sorted order.
    """
    return sorted(set(tup1) | set(tup2))

print(union_elements((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 4, 5, 6, 7, 10))

# Output: True

# Test case 2
print(union_elements((1, 2, 3, 4), (3, 4, 5, 6)) == (1, 2, 3, 4, 5, 6))

# Output: True

# Test case 3
print(union_elements((1, 2, 3), (4, 5, 6)) == (1, 2, 3, 4, 5, 6))

# Output: True

# Test case 4
print(union_elements((), (4, 5, 6)) == (4, 5, 6)

# Output: True

# Test case 5
print(union_elements((1, 2, 3, 4), ()) == (1, 2, 3, 4)

# Output: True

# Test case 6
print(union_elements((), ()) == ()

# Output: True

# Test case 7
print(union_elements((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

# Output: True

# Test case 8
print(union_elements((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12) == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

# Output: True

# Test case 9
print(union_elements((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12) == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

# Output: True

# Test case 10
print(union_elements((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12) == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

# Output: True

# Test case 11
print(union_elements((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12) == (1,