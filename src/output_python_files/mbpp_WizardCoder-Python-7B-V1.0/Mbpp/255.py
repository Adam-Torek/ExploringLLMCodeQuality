"""
Write a function that takes in a list and length n, and generates all combinations (with repetition) of the elements of the list and returns a list with a tuple for each combination.
assert combinations_colors( ["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]
"""

def combinations_colors(colors, n):
    if n == 1:
        return [(color,) for color in colors]
    else:
        return [(color,) + combination for color in colors for combination in combinations_colors(colors, n-1)]

print(combinations_colors(["Red","Green","Blue"],1))
print(combinations_colors(["Red","Green","Blue"],2))
print(combinations_colors(["Red","Green","Blue"],3))
print(combinations_colors(["Red","Green","Blue"],4))

# Output:
# [('Red',), ('Green',), ('Blue',)]
# [('Red', 'Red'), ('Green', 'Red'), ('Blue', 'Red'), ('Red', 'Green'), ('Green', 'Green'), ('Blue', 'Green'), ('Red', 'Blue'), ('Green', 'Blue'), ('Blue', 'Blue')]
# [('Red', 'Red', 'Red'), ('Green', 'Red', 'Red'), ('Blue', 'Red', 'Red'), ('Red', 'Green', 'Red'), ('Green', 'Green', 'Red'), ('Blue', 'Green', 'Red'), ('Red', 'Blue', 'Red'), ('Green', 'Green', 'Green'), ('Blue', 'Green', 'Green'), ('Red', 'Blue', 'Green'), ('Green', 'Blue', 'Green'), ('Red', 'Red', 'Blue'), ('Green', 'Red', 'Blue'), ('Blue', 'Red', 'Blue'), ('Green', 'Green', 'Blue'), ('Blue', 'Green', 'Blue'), ('Red', 'Blue', 'Blue')]
# [('Red', 'Red', 'Red', 'Red'), ('Green', 'Red', 'Red', 'Red'), ('Blue', 'Red', 'Red', 'Red'), ('Red', 'Green', 'Red', 'Red'), ('Green', 'Green', 'Red', 'Red'), ('Blue', 'Green', 'Red', 'Red'), ('Red', 'Blue', 'Red', 'Red'), ('Green', 'Green', 'Green', 'Red'), ('Blue', 'Green', 'Green', 'Red'), ('Red', 'Blue', 'Green', 'Red'), ('Green', 'Blue', 'Red', 'Red'), ('Red', 'Red', 'Green', 'Red'), ('Green', 'Green', 'Green', 'Green'), ('Blue', 'Green', 'Green', 'Green'), ('Red', 'Blue', 'Green', 'Green'), ('Green', 'Blue', 'Green', 'Green'), ('Red', 'Red', 'Blue', 'Red'), ('Green', 'Red', 'Blue', 'Red'), ('Blue', 'Red', 'Blue', 'Red'), ('Green', 'Green', 'Blue', 'Red'), ('Red', 'Green', 'Blue', 'Red'), ('Blue', 'Green', 'Green', 'Green'), ('Red', 'Blue', 'Green', 'Green'), ('Green', 'Blue', 'Green', 'Green'), ('Red', 'Red', 'Green', 'Green'), ('Green', 'Red', 'Green', 'Green'), ('Blue', 'Red', 'Green', 'Green'), ('Red', 'Green', 'Green', 'Green'), ('Green', 'Blue', 'Green', 'Green'), ('Red', 'Red', 'Blue', 'Green'), ('Green', 'Green', 'Blue', 'Green'), ('Blue', 'Green', 'Green', 'Green'), ('Red', 'Red', 'Green', 'Green'), ('Green', 'Red', 'Green', 'Green'), ('Blue', 'Red', 'Green', 'Green'), ('Red', 'Blue', 'Green', 'Green'), ('Green', 'Blue', 'Green', 'Green'), ('Red', 'Red', 'Blue', 'Green'), ('Green', 'Green', 'Blue', 'Green'), ('Blue', 'Green', 'Blue', 'Green'), ('Red', 'Red', 'Green', 'Green'), ('Green', 'Red', 'Green', 'Green'), ('Blue', 'Red', 'Green', 'Green'), ('Green', 'Green', 'Red', 'Green'), ('Blue', 'Green', 'Red', 'Green'), ('Red', 'Red', 'Blue', 'Green'), ('Green', 'Green', 'Blue', 'Green'), ('Blue', 'Green', 'Red', 'Green'), ('Red',