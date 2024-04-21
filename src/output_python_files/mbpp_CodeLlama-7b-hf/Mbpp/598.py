"""
Write a function to check whether the given number is armstrong or not.
assert armstrong_number(153)==True
"""


def armstrong_number(n):
    """
    :param n: int
    :return: bool
    """
    if n < 0:
        return False
    else:
        n_list = list(str(n))
        n_len = len(n_list)
        n_sum = 0
        for i in n_list:
            n_sum += int(i) ** n_len
        if n_sum == n:
            return True
        else:
            return False


if __name__ == '__main__':
    print(armstrong_number(153))
    print(armstrong_number(123))
    print(armstrong_number(100))
    print(armstrong_number(1000))
    print(armstrong_number(10000))
    print(armstrong_number(100000))
    print(armstrong_number(1000000))
    print(armstrong_number(10000000))
    print(armstrong_number(100000000))
    print(armstrong_number(1000000000))
    print(armstrong_number(10000000000))
    print(armstrong_number(100000000000))
    print(armstrong_number(1000000000000))
    print(armstrong_number(10000000000000))
    print(armstrong_number(100000000000000))
    print(armstrong_number(1000000000000000))
    print(armstrong_number(10000000000000000))
    print(armstrong_number(100000000000000000))
    print(armstrong_number(1000000000000000000))
    print(armstrong_number(10000000000000000000))
    print(armstrong_number(100000000000000000000))
    print(armstrong_number(1000000000000000000000))
    print(armstrong_number(10000000000000000000000))
    print(armstrong_number(100000000000000000000000))
    print(armstrong_number(1000000000000000000000000))
    print(armstrong_number(10000000000000000000000000))
    print(armstrong_number(100000000000000000000000000))
    print(armstrong_number(1000000000000000000000000000))
    print(armstrong_number(10000000000000000000000000000))
    print(armstrong_number(100000000000000000000000000000))
    print(armstrong_number(1000000000000000000000000000000))
    print(armstrong_number(10000000000000000000000000000000))
    print(