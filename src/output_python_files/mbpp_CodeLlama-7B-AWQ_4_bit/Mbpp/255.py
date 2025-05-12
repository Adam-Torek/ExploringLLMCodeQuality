"""
Write a function that takes in a list and length n, and generates all combinations (with repetition) of the elements of the list and returns a list with a tuple for each combination.
assert combinations_colors( ["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]
"""


def combinations_colors(colors, n):
    """
    Write a function that takes in a list and length n, and generates all combinations (with repetition) of the elements of the list and returns a list with a tuple for each combination.
    assert combinations_colors( ["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]
    """
    if n == 1:
        return [(color,) for color in colors]
    else:
        return [
            (color,) + combination
            for color in colors
            for combination in combinations_colors(colors, n - 1)
        ]


if __name__ == "__main__":
    print(combinations_colors(["Red", "Green", "Blue"], 1))
    print(combinations_colors(["Red", "Green", "Blue"], 2))
    print(combinations_colors(["Red", "Green", "Blue"], 3))
    print(combinations_colors(["Red", "Green", "Blue"], 4))
    print(combinations_colors(["Red", "Green", "Blue"], 5))
    print(combinations_colors(["Red", "Green", "Blue"], 6))
    print(combinations_colors(["Red", "Green", "Blue"], 7))
    print(combinations_colors(["Red", "Green", "Blue"], 8))
    print(combinations_colors(["Red", "Green", "Blue"], 9))
    print(combinations_colors(["Red", "Green", "Blue"], 10))
    print(combinations_colors(["Red", "Green", "Blue"], 11))
    print(combinations_colors(["Red", "Green", "Blue"], 12))
    print(combinations_colors(["Red", "Green", "Blue"], 13))
    print(combinations_colors(["Red", "Green", "Blue"], 14))
    print(combinations_colors(["Red", "Green", "Blue"], 15))
    print(combinations_colors(["Red", "Green", "Blue"], 16))
    print(combinations_colors(["Red", "Green", "Blue"], 17))
    print(combinations_colors(["Red", "Green", "Blue"], 18))
    print(combinations_colors(["Red", "Green", "Blue"], 19))
    print(combinations_colors(["Red", "Green", "Blue"], 20))
    print(combinations_colors(["Red", "Green", "Blue"], 21))
    print(combinations_colors(["Red", "Green", "Blue"], 22))
    print(combinations_colors(["Red", "Green", "Blue"], 23))
    print(combinations_colors(["Red", "Green", "Blue"], 24))
    print(combinations_colors(["Red", "Green", "Blue"], 25))
    print(combinations_colors(["Red", "Green", "Blue"], 26))
    print(combinations_colors(["Red", "Green", "Blue"], 27))
    print(combinations_colors(["Red", "Green", "Blue"], 28))
    print(combinations_colors(["Red", "Green", "Blue"], 29))
    print(combinations_colors(["Red", "Green", "Blue"], 30))
    print(combinations_colors(["Red", "Green", "Blue"], 31))
    print(combinations_colors(["Red", "Green", "Blue"], 32))
    print(combinations_colors(["Red", "Green", "Blue"], 33))
    print(combinations_colors(["Red", "Green", "Blue"], 34))
    print(combinations_colors(["Red", "Green",