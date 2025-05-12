"""
Write a function to find sum and average of first n natural numbers.
assert sum_average(10)==(55, 5.5)
"""


def sum_average(n):
    """
    :param n: int
    :return: (int, float)
    """
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum, sum / n


if __name__ == '__main__':
    print(sum_average(10))
    print(sum_average(100))
    print(sum_average(1000))
    print(sum_average(10000))
    print(sum_average(100000))
    print(sum_average(1000000))
    print(sum_average(10000000))
    print(sum_average(100000000))
    print(sum_average(1000000000))
    print(sum_average(10000000000))
    print(sum_average(100000000000))
    print(sum_average(1000000000000))
    print(sum_average(10000000000000))
    print(sum_average(100000000000000))
    print(sum_average(1000000000000000))
    print(sum_average(10000000000000000))
    print(sum_average(100000000000000000))
    print(sum_average(1000000000000000000))
    print(sum_average(10000000000000000000))
    print(sum_average(100000000000000000000))
    print(sum_average(1000000000000000000000))
    print(sum_average(10000000000000000000000))
    print(sum_average(100000000000000000000000))
    print(sum_average(1000000000000000000000000))
    print(sum_average(10000000000000000000000000))
    print(sum_average(100000000000000000000000000))
    print(sum_average(1000000000000000000000000000))
    print(sum_average(10000000000000000000000000000))
    print(sum_average(100000000000000000000000000000))
    print(sum_average(1000000000000000000000000000000))
    print(sum_average(10000000000000000000000000000000))
    print(sum_average(100000000000000000000000000000000))
    print(sum_average(100000000000000