"""
Write a function that takes in a list and an integer n and returns a list containing the n largest items from the list.
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
"""


def larg_nnum(lst, n):
    """
    :param lst: list
    :param n: int
    :return: list
    """
    if n > len(lst):
        return lst
    else:
        lst.sort(reverse=True)
        return lst[:n]


if __name__ == '__main__':
    print(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 2))
    print(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 3))
    print(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 4))
    print(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 5))
    print(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 6))
    print(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 7))
    print(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 8))
    print(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 9))
    print(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 10))
    print(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 11))
    print(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 12))
    print(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 13))
    print(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 14))
    print(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 15))
    print(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100