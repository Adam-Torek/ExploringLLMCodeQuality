"""
Write a function to find the maximum sum possible by using the given equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n).
assert get_max_sum(60) == 106
"""


def get_max_sum(n):
    """
    :param n: int
    :return: int
    """
    if n < 2:
        return n
    else:
        return max(get_max_sum(n // 2) + get_max_sum(n // 3) + get_max_sum(n // 4) + get_max_sum(n // 5), n)


if __name__ == '__main__':
    print(get_max_sum(60))
    print(get_max_sum(100))
    print(get_max_sum(1000))
    print(get_max_sum(10000))
    print(get_max_sum(100000))
    print(get_max_sum(1000000))
    print(get_max_sum(10000000))
    print(get_max_sum(100000000))
    print(get_max_sum(1000000000))
    print(get_max_sum(10000000000))
    print(get_max_sum(100000000000))
    print(get_max_sum(1000000000000))
    print(get_max_sum(10000000000000))
    print(get_max_sum(100000000000000))
    print(get_max_sum(1000000000000000))
    print(get_max_sum(10000000000000000))
    print(get_max_sum(100000000000000000))
    print(get_max_sum(1000000000000000000))
    print(get_max_sum(10000000000000000000))
    print(get_max_sum(100000000000000000000))
    print(get_max_sum(1000000000000000000000))
    print(get_max_sum(10000000000000000000000))
    print(get_max_sum(100000000000000000000000))
    print(get_max_sum(1000000000000000000000000))
    print(get_max_sum(10000000000000000000000000))
    print(get_max_sum(100000000000000000000000000))
    print(get_max_sum(1000000000000000000000000000))
    print(get_max_sum(10000000000000000000000000000))
    print(get_max_sum(100000000000000000000000000000))
    print(get_max_sum(1000000000000000000000000000000))
    print(get_max_sum(10