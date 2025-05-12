"""
Write a python function to count the number of equal numbers from three given integers.
assert test_three_equal(1,1,1) == 3
"""


def test_three_equal(a, b, c):
    if a == b and b == c:
        return 3
    elif a == b or b == c or a == c:
        return 2
    else:
        return 0


if __name__ == '__main__':
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
    print(test_three_equal(1, 1, 2))
    print(test_three_equal(1, 2, 3))
    print(test_three_equal(1, 2, 4))
    print(test_three_equal(1, 3, 4))
    print(test_three_equal(2, 3, 4))
    print(test_three_equal(1, 1, 3))
    print(test_three_equal(1, 1, 4))
    print(test_three_equal(1, 2, 4))
    print(test_three_equal(1, 3, 4))
    print(test_three_equal(2, 3, 4))
    print(test_three_equal(1, 1, 4))
    print(test_three_equal(1, 2, 4))
    print(test_three_equal(1, 3, 4))
    print(test_three_equal(2, 3, 4))
    print(test_three_equal(1, 1, 4))
    print(test_three_equal(1, 2, 4))
    print(test_three_equal(1, 3, 4))
    print(test_three_equal(2, 3, 4))
    print(test_three_equal(1, 1, 4))
    print(test_three_equal(1, 2, 4))
    print(test_three_equal(1, 3, 4))
    print(test_three_equal(2, 3, 4))
    print(test_three_equal(1, 1, 4))
    print(test_three_equal(1, 2, 4))
    print(test_three_equal(1, 3, 4))
    print(test_three_equal(2, 3, 4))
    print(test_three_equal(1, 1, 4))
    print(test_three_equal(1, 2, 4))
    print(test_three_equal(1, 3, 4))
    print(test_three_equal(2, 3, 4))
    print(test_three_equal(1, 1, 4))
    print(test_three_equal(1, 2, 4))
    print