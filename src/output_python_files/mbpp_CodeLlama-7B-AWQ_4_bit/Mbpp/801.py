"""
Write a python function to count the number of equal numbers from three given integers.
assert test_three_equal(1,1,1) == 3
"""


def test_three_equal(a, b, c):
    if a == b and b == c:
        return 3
    elif a == b:
        return 2
    elif a == c:
        return 2
    elif b == c:
        return 2
    else:
        return 0


print(test_three_equal(1, 1, 1))
print(test_three_equal(1, 1, 2))
print(test_three_equal(1, 2, 2))
print(test_three_equal(1, 2, 3))
print(test_three_equal(1, 2, 4))
print(test_three_equal(1, 3, 3))
print(test_three_equal(1, 3, 4))
print(test_three_equal(1, 4, 4))
print(test_three_equal(2, 2, 2))
print(test_three_equal(2, 2, 3))
print(test_three_equal(2, 2, 4))
print(test_three_equal(2, 3, 3))
print(test_three_equal(2, 3, 4))
print(test_three_equal(2, 4, 4))
print(test_three_equal(3, 3, 3))
print(test_three_equal(3, 3, 4))
print(test_three_equal(3, 4, 4))
print(test_three_equal(4, 4, 4))
print(test_three_equal(4, 4, 5))
print(test_three_equal(4, 5, 5))
print(test_three_equal(5, 5, 5))
print(test_three_equal(5, 5, 6))
print(test_three_equal(5, 6, 6))
print(test_three_equal(6, 6, 6))
print(test_three_equal(6, 6, 7))
print(test_three_equal(6, 7, 7))
print(test_three_equal(7, 7, 7))
print(test_three_equal(7, 7, 8))
print(test_three_equal(7, 8, 8))
print(test_three_equal(8, 8, 8))
print(test_three_equal(8, 8, 9))
print(test_three_equal(8, 9, 9))
print(test_three_equal(9, 9, 9))
print(test_three_equal(9, 9, 10))
print(test_three_equal(9, 10, 10))
print(test_three_equal(10, 10, 10))
print(test_three_equal(10, 10, 11))
print(test_three_equal(10, 11, 11))
print(test_three_equal(11, 11, 11))
print(test_three_equal(11, 11, 12))
print(test_three_equal(11, 12, 12))
print(test_three_equal(12, 12, 12))
print(test_three_equal(12, 12, 13))
print(test_three_equal(12, 13, 13))
print(test_three_equal(13, 13, 13))
print(test_three_equal(13, 13, 14))
print(test_three_equal(13, 14, 14))
print(test_three_equal(14, 14, 14))
print(test_three_equal(14, 14, 15))
print(test_three_equal(14, 15, 15))