"""
Write a function to check if each element of second tuple is smaller than its corresponding element in the first tuple.
assert check_smaller((1, 2, 3), (2, 3, 4)) == False
"""


def check_smaller(t1, t2):
    """
    Check if each element of second tuple is smaller than its corresponding element in the first tuple.
    :param t1: tuple
    :param t2: tuple
    :return: bool
    """
    if len(t1) != len(t2):
        return False
    for i in range(len(t1)):
        if t1[i] > t2[i]:
            return False
    return True


if __name__ == '__main__':
    print(check_smaller((1, 2, 3), (2, 3, 4)))
    print(check_smaller((1, 2, 3), (2, 3, 3)))
    print(check_smaller((1, 2, 3), (2, 3, 2)))
    print(check_smaller((1, 2, 3), (2, 3, 1)))
    print(check_smaller((1, 2, 3), (2, 3, 0)))
    print(check_smaller((1, 2, 3), (2, 3, -1)))
    print(check_smaller((1, 2, 3), (2, 3, -2)))
    print(check_smaller((1, 2, 3), (2, 3, -3)))
    print(check_smaller((1, 2, 3), (2, 3, -4)))
    print(check_smaller((1, 2, 3), (2, 3, -5)))
    print(check_smaller((1, 2, 3), (2, 3, -6)))
    print(check_smaller((1, 2, 3), (2, 3, -7)))
    print(check_smaller((1, 2, 3), (2, 3, -8)))
    print(check_smaller((1, 2, 3), (2, 3, -9)))
    print(check_smaller((1, 2, 3), (2, 3, -10)))
    print(check_smaller((1, 2, 3), (2, 3, -11)))
    print(check_smaller((1, 2, 3), (2, 3, -12)))
    print(check_smaller((1, 2, 3), (2, 3, -13)))
    print(check_smaller((1, 2, 3), (2, 3, -14)))
    print(check_smaller((1, 2, 3), (2, 3, -15)))
    print(check_smaller((1, 2, 3), (2, 3, -16)))
    print(check_smaller((1, 2, 3), (2, 3, -17)))
    print(check_smaller((1, 2, 3), (2, 3, -18)))
    print(check_smaller((1, 2, 3), (2, 3, -19)))
    print(check_smaller((1, 2, 3), (2, 3, -20)))
    print(check_smaller((1, 2, 3), (2, 3, -21)))
    print(check_smaller((1, 2, 3), (2, 3, -22)))
    print(check_smaller((1, 2, 3), (2, 3, -23)))
    print(check_smaller((1, 2, 3), (2, 3, -24)))
    print(check_smaller((1, 2, 3), (2, 3, -25)))
    print(check_smaller((1, 2, 3), (2, 3, -26)))
    print(check_smaller((1, 2, 3), (2