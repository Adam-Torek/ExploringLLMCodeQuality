"""
Write a function that takes in two tuples and subtracts the elements of the first tuple by the elements of the second tuple with the same index.
assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
"""

def substract_elements(tup1, tup2):
    return tuple(tup1[i] - tup2[i] for i in range(len(tup1)))

print(substract_elements((10, 4, 5), (2, 5, 18))) # Output: (8, -1, -13)
print(substract_elements((1, 2, 3), (4, 5, 6))) # Output: (-3, -3, -3)
print(substract_elements((10, 20, 30), (2, 5, 18))) # Output: (8, 15, 12)