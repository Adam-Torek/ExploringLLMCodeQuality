"""
Write a python function to count the number of equal numbers from three given integers.
assert test_three_equal(1,1,1) == 3
"""

def test_three_equal(a, b, c):
    if a == b and b == c:
        return 3
    else:
        return 0


def count_three_equal(a, b, c):
    if a == b and b == c:
        return 3
    elif a == b or b == c or a == c:
        return 2
    else:
        return 0


# test the function
print(count_three_equal(1, 1, 1))