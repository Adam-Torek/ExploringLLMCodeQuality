"""
Write a python function takes in an integer n and returns the sum of squares of first n even natural numbers.
assert square_Sum(2) == 20
"""
def square_sum(n):
    """
    :param n: an integer
    :return: the sum of squares of first n even natural numbers
    """
    sum = 0
    for i in range(n):
        if i % 2 == 0:
            sum += i * i
    return sum

assert square_sum(2) == 20
assert square_sum(5) == 100
assert square_sum(10) == 3850
assert square_sum(1) == 1
assert square_sum(0) == 0