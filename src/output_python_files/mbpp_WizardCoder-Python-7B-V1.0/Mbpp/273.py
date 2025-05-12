"""
Write a function that takes in two tuples and subtracts the elements of the first tuple by the elements of the second tuple with the same index.
assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
"""

def substract_elements(tup1, tup2):
    result = []
    for i in range(len(tup1)):
        result.append(tup1[i] - tup2[i])
    return tuple(result)

print(substract_elements((10, 4, 5), (2, 5, 18))) # Output: (8, -1, -13)
print(substract_elements((10, 4, 5), (2, 5, 18, 3)) # Output: (8, -1, -13, 3)
print(substract_elements((10, 4), (2, 5, 18)) # Output: (8, -1)