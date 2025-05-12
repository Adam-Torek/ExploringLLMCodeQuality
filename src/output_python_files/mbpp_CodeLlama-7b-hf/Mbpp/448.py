"""
Write a function to calculate the sum of perrin numbers.
assert cal_sum(9) == 49
"""


def cal_sum(n):
    """
    :param n: int
    :return: int
    """
    if n == 1:
        return 1
    else:
        return n + cal_sum(n - 1)


if __name__ == '__main__':
    print(cal_sum(9))