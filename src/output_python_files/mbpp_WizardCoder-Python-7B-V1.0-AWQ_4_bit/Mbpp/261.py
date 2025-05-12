"""
Write a function that takes in two tuples and performs mathematical division operation element-wise across the given tuples.
assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)
"""

def division_elements(tup1, tup2):
    if len(tup1) != len(tup2):
        return "Tuples must be of same length"
    else:
        result = []
        for i in range(len(tup1)):
            result.append(tup1[i] / tup2[i])
        return tuple(result)

print(division_elements((10, 4, 6, 9),(5, 2, 3, 3)) # Output: (2, 2, 2, 3)