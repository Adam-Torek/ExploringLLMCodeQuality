"""
Write a python function that takes in an integer n and returns the sum of the squares of the first n odd natural numbers.
assert square_Sum(2) == 10
"""


def square_Sum(n):
    """
    :param n: int
    :return: int
    """
    sum = 0
    for i in range(1, n + 1, 2):
        sum += i ** 2
    return sum


if __name__ == '__main__':
    print(square_Sum(2))
    print(square_Sum(5))
    print(square_Sum(10))
    print(square_Sum(100))
    print(square_Sum(1000))
    print(square_Sum(10000))
    print(square_Sum(100000))
    print(square_Sum(1000000))
    print(square_Sum(10000000))
    print(square_Sum(100000000))
    print(square_Sum(1000000000))
    print(square_Sum(10000000000))
    print(square_Sum(100000000000))
    print(square_Sum(1000000000000))
    print(square_Sum(10000000000000))
    print(square_Sum(100000000000000))
    print(square_Sum(1000000000000000))
    print(square_Sum(10000000000000000))
    print(square_Sum(100000000000000000))
    print(square_Sum(1000000000000000000))
    print(square_Sum(10000000000000000000))
    print(square_Sum(100000000000000000000))
    print(square_Sum(1000000000000000000000))
    print(square_Sum(10000000000000000000000))
    print(square_Sum(100000000000000000000000))
    print(square_Sum(1000000000000000000000000))
    print(square_Sum(10000000000000000000000000))
    print(square_Sum(100000000000000000000000000))
    print(square_Sum(1000000000000000000000000000))
    print(square_Sum(10000000000000000000000000000))
    print(square_Sum(100000000000000000000000000000))
    print(square_Sum(1000000000000000000000000000000))
    print(square_Sum(10000000000000000000000000000000))
    print(square_Sum(100000000000000000000000000000000))
    print(square_Sum(1000000000000000000000000000