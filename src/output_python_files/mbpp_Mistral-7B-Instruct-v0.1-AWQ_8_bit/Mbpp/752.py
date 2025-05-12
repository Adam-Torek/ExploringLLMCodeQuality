"""
Write a function to find the nth jacobsthal number. https://www.geeksforgeeks.org/jacobsthal-and-jacobsthal-lucas-numbers/ 0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731, ...
assert jacobsthal_num(5) == 11
"""

def jacobsthal_num(n):
    """
    :param n:
    :return:
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n % 2 == 0:
        return jacobsthal_num(n // 2) * 3
    else:
        return jacobsthal_num(n // 2) * 4


if __name__ == '__main__':
    print(jacobsthal_num(5))