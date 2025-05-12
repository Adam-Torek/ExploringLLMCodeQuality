"""
Write a function to determine if the sum of the divisors of two integers are the same.
assert are_equivalent(36, 57) == False
"""


def are_equivalent(a, b):
    """
    :param a: int
    :param b: int
    :return: bool
    """
    return sum_of_divisors(a) == sum_of_divisors(b)


def sum_of_divisors(n):
    """
    :param n: int
    :return: int
    """
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)


if __name__ == '__main__':
    print(are_equivalent(36, 57))
    print(are_equivalent(12, 28))
    print(are_equivalent(12, 24))
    print(are_equivalent(12, 20))
    print(are_equivalent(12, 18))
    print(are_equivalent(12, 16))
    print(are_equivalent(12, 14))
    print(are_equivalent(12, 12))
    print(are_equivalent(12, 10))
    print(are_equivalent(12, 8))
    print(are_equivalent(12, 6))
    print(are_equivalent(12, 4))
    print(are_equivalent(12, 2))
    print(are_equivalent(12, 1))
    print(are_equivalent(12, 0))
    print(are_equivalent(12, -1))
    print(are_equivalent(12, -2))
    print(are_equivalent(12, -4))
    print(are_equivalent(12, -6))
    print(are_equivalent(12, -8))
    print(are_equivalent(12, -10))
    print(are_equivalent(12, -12))
    print(are_equivalent(12, -14))
    print(are_equivalent(12, -16))
    print(are_equivalent(12, -18))
    print(are_equivalent(12, -20))
    print(are_equivalent(12, -22))
    print(are_equivalent(12, -24))
    print(are_equivalent(12, -26))
    print(are_equivalent(12, -28))
    print(are_equivalent(12, -30))
    print(are_equivalent(12, -32))
    print(are_equivalent(12, -34))
    print(are_equivalent(12, -36))
    print(are_equivalent(12, -38))
    print(are_equivalent(12, -40))
    print(are_equivalent(12, -42))
    print(are_equivalent(12, -44))
    print(are_equivalent(12, -46))
    print(are_equivalent(12, -48))
    print(are_equivalent(12, -50))
    print(are_equivalent(12, -52))
    print(are_equivalent(12, -54))
    print(are_equivalent(12, -56))
    print(are_equivalent(12, -58))
    print(are_equivalent(12, -60))
    print(are_equivalent(12, -62))
    print(are_equivalent(12, -64))
    print(are_equivalent(12, -66))
    print(