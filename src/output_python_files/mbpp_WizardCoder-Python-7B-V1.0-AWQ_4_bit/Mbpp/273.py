"""
Write a function that takes in two tuples and subtracts the elements of the first tuple by the elements of the second tuple with the same index.
assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
"""

def substract_elements(t1, t2):
    return tuple(t1[i] - t2[i] for i in range(len(t1)))

print(substract_elements((10, 4, 5), (2, 5, 18))) # Output: (8, -1, -13)
print(substract_elements((1, 2, 3), (4, 5, 6))) # Output: (-3, -3, -3)
print(substract_elements((1, 2, 3, 4), (5, 6, 7, 8))) # Output: (-4, -4, -5, -5)