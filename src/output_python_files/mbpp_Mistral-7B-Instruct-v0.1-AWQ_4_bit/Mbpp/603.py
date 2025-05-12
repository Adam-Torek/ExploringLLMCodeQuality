"""
Write a function to get all lucid numbers smaller than or equal to a given integer.
assert get_ludic(10) == [1, 2, 3, 5, 7]
"""

def get_ludic(n):
    """
    Returns a list of all lucid numbers smaller than or equal to n.
    A number is lucid if it is the sum of an arithmetic sequence with a common difference of 1.
    """
    ludic = []
    for i in range(1, n+1):
        for j in range(i, n+1):
            if i + j <= n and (i+j) % 2 == 1:
                ludic.append(i+j)
    return ludic

assert get_ludic(10) == [1, 2, 3, 5, 7]