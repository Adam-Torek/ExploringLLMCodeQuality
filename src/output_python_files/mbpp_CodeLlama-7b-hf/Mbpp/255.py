"""
Write a function that takes in a list and length n, and generates all combinations (with repetition) of the elements of the list and returns a list with a tuple for each combination.
assert combinations_colors( ["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]
"""

def combinations_colors(colors, n):
    if n == 0:
        return [()]
    else:
        return [(*t, color) for t in combinations_colors(colors, n-1) for color in colors]