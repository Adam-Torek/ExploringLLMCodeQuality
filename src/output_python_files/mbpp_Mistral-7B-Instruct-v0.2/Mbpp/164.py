"""
Write a function to determine if the sum of the divisors of two integers are the same.
assert are_equivalent(36, 57) == False
"""
from math import sqrt

def are_equivalent(num1, num2):
    """
    Determines if the sum of the divisors of two integers are the same
    :param num1: int
    :param num2: int
    :return: bool
    """
    divisors_sum_num1 = sum(list(divisors(num1)))
    divisors_sum_num2 = sum(list(divisors(num2)))
    return divisors_sum_num1 == divisors_sum_num2

def divisors(n):
    """
    Generates a list of divisors of a given number
    :param n: int
    :return: list
    """
    divisors = [1]
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(int(n/i))
    if sqrt(n).is_integer():
        divisors.append(int(sqrt(n)))
    return divisors

if __name__ == "__main__":
    assert are_equivalent(36, 57) == False
    assert are_equivalent(28, 28) == True
    assert are_equivalent(12, 12) == True
    assert are_equivalent(15, 15) == True
    assert are_equivalent(10, 10) == True
    assert are_equivalent(1, 1) == True
    assert are_equivalent(1, 2) == False
    assert are_equivalent(1, 3) == False
    assert are_equivalent(1, 4) == False
    assert are_equivalent(1, 5) == False
    assert are_equivalent(1, 6) == False
    assert are_equivalent(1, 7) == False
    assert are_equivalent(1, 8) == False
    assert are_equivalent(1, 9) == False
    assert are_equivalent(1, 10) == False
    assert are_equivalent(1, 11) == False
    assert are_equivalent(1, 12) == False
    assert are_equivalent(1, 13) == False
    assert are_equivalent(1, 14) == False
    assert are_equivalent(1, 15) == False
    assert are_equivalent(1, 16) == False
    assert are_equivalent(1, 17) == False
    assert are_equivalent(1, 18) == False
    assert are_equivalent(1, 19) == False
    assert are_equivalent(1, 20) == False
    assert are_equivalent(1, 21) == False
    assert are_equivalent(1, 22) == False
    assert are_equivalent(1, 23) == False
    assert are_equivalent(1, 24) == False
    assert are_equivalent(1, 25) == False
    assert are_equivalent(1, 26) == False
    assert are_equivalent(1, 27) == False
    assert are_equivalent(1, 28) == False
    assert are_equivalent(1, 29) == False
    assert are_equivalent(1, 30) == False
    assert are_equivalent(1, 31) == False
    assert are_equivalent(1, 32) == False
    assert are_equivalent(1, 33) == False
    assert are_equivalent(1, 34) == False
    assert are_equivalent(1, 35) == False
    assert are_equivalent(1, 36) == False
    assert are_equivalent(1, 37) == False