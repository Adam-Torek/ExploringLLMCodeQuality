"""
Write a function that takes in a list and length n, and generates all combinations (with repetition) of the elements of the list and returns a list with a tuple for each combination.
assert combinations_colors( ["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]
"""
def combinations_colors(colors, n):
    """
    :param colors: list of colors
    :param n: length of the combinations
    :return: list of tuples with all combinations of colors
    """
    if n == 1:
        return colors
    else:
        result = []
        for i in range(n):
            result.append(colors[i])
            result.append(combinations_colors(colors, n-1))
        return result


def test_combinations_colors():
    """
    Test the combinations_colors function
    """
    assert combinations_colors(["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]
    assert combinations_colors(["Red","Green","Blue"],2)==[('Red', 'Green'), ('Red', 'Blue'), ('Green', 'Blue')]
    assert combinations_colors(["Red","Green","Blue"],3)==[('Red', 'Green', 'Blue')]


if __name__ == '__main__':
    test_combinations_colors()