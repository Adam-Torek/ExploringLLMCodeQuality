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
        num_list = list(str(n))
        num_list_len = len(num_list)
        num_list_sum = 0
        for i in num_list:
            num_list_sum += int(i) ** num_list_len
        if num_list_sum == n:
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
    print(armstrong_number(