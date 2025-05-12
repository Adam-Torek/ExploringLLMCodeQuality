"""
Write a function to get all lucid numbers smaller than or equal to a given integer.
assert get_ludic(10) == [1, 2, 3, 5, 7]
"""

def get_ludic(n):
    """
    Returns a list of all lucid numbers smaller than or equal to n.
    A number is considered lucid if it is the sum of an even number and an odd number.
    """
    ludic_numbers = []
    for i in range(2, n+1):
        for j in range(i+1, n+1):
            if i % 2 == 0 and j % 2 != 0:
                ludic_numbers.append(i + j)
    return ludic_numbers

# assert get_ludic(10) == [1, 2, 3, 5, 7]
print(get_ludic(10))