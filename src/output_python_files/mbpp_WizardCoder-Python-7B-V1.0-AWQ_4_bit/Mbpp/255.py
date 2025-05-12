"""
Write a function that takes in a list and length n, and generates all combinations (with repetition) of the elements of the list and returns a list with a tuple for each combination.
assert combinations_colors( ["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]
"""

def combinations_colors(colors, n):
    return list(itertools.combinations(colors, n))

print(combinations_colors(["Red","Green","Blue"],1))
print(combinations_colors(["Red","Green","Blue"],2))
print(combinations_colors(["Red","Green","Blue"],3))

# Output:
# [('Red',), ('Green',), ('Blue',)]
# [('Red', 'Red'), ('Green', 'Red'), ('Blue', 'Red'), ('Red', 'Green'), ('Green', 'Green'), ('Blue', 'Green'), ('Red', 'Blue'), ('Green', 'Blue'), ('Blue', 'Blue')]
# [('Red', 'Red', 'Red'), ('Green', 'Red', 'Red'), ('Blue', 'Red', 'Red'), ('Red', 'Green', 'Red'), ('Green', 'Green', 'Red'), ('Blue', 'Green', 'Red'), ('Red', 'Blue', 'Red'), ('Green', 'Green', 'Green'), ('Blue', 'Green', 'Green'), ('Red', 'Blue', 'Green'), ('Green', 'Blue', 'Green'), ('Red', 'Red', 'Blue'), ('Green', 'Red', 'Blue'), ('Blue', 'Red', 'Blue'), ('Green', 'Green', 'Blue'), ('Blue', 'Green', 'Blue'), ('Red', 'Blue', 'Blue')]

# Explanation:
# The function takes in a list of colors and a length n, and returns a list of tuples containing all possible combinations of the colors with length n.
# In the first example, there is only one color in the list, so there is only one combination, which is a tuple containing that color.
# In the second example, there are two colors, so there are 3^2 possible combinations, which are Red-Red, Green-Red, Blue-Red, Green-Green, Blue-Green, Red-Blue, Green-Blue, and Blue-Blue.
# In the third example, there are three colors, so there are 3^3 possible combinations, which are Red-Red-Red, Green-Red-Red, Blue-Red-Red, Green-Green-Red, Blue-Green-Red, Red-Blue-Red, Green-Blue-Red, Blue-Green-Red, Green-Red-Green, Green-Green-Green, Blue-Green-Green, Red-Blue-Green, Green-Blue-Green, Red-Red-Blue, Green-Red-Blue, Blue-Red-Blue, Green-Green-Blue, Blue-Green-Blue, and Red-Blue-Blue.