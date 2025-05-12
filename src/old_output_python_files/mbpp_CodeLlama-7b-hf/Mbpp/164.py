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
    return sum(divisors(a)) == sum(divisors(b))


def divisors(n):
    """
    :param n: int
    :return: list
    """
    return [i for i in range(1, n + 1) if n % i == 0]


if __name__ == '__main__':
    print(are_equivalent(36, 57))
    print(are_equivalent(12, 18))
    print(are_equivalent(12, 24))
    print(are_equivalent(12, 25))
    print(are_equivalent(12, 26))
    print(are_equivalent(12, 27))
    print(are_equivalent(12, 28))
    print(are_equivalent(12, 29))
    print(are_equivalent(12, 30))
    print(are_equivalent(12, 31))
    print(are_equivalent(12, 32))
    print(are_equivalent(12, 33))
    print(are_equivalent(12, 34))
    print(are_equivalent(12, 35))
    print(are_equivalent(12, 36))
    print(are_equivalent(12, 37))
    print(are_equivalent(12, 38))
    print(are_equivalent(12, 39))
    print(are_equivalent(12, 40))
    print(are_equivalent(12, 41))
    print(are_equivalent(12, 42))
    print(are_equivalent(12, 43))
    print(are_equivalent(12, 44))
    print(are_equivalent(12, 45))
    print(are_equivalent(12, 46))
    print(are_equivalent(12, 47))
    print(are_equivalent(12, 48))
    print(are_equivalent(12, 49))
    print(are_equivalent(12, 50))
    print(are_equivalent(12, 51))
    print(are_equivalent(12, 52))
    print(are_equivalent(12, 53))
    print(are_equivalent(12, 54))
    print(are_equivalent(12, 55))
    print(are_equivalent(12, 56))
    print(are_equivalent(12, 57))
    print(are_equivalent(12, 58))
    print(are_equivalent(12, 59))
    print(are_equivalent(12, 60))
    print(are_equivalent(12, 61))
    print(are_equivalent(12, 62))
    print(are_equivalent(12, 63))
    print(are_equivalent(12, 64))
    print(are_equivalent(12, 65))
    print(are_equivalent(12, 66))
    print(are_equivalent(12, 67))
    print(are_equivalent(12, 68))
    print(are_equivalent(12, 69))
    print(are_equivalent(12, 70))
    print(are_equivalent(12, 71))
    print(are_equivalent(12, 72))
    print(are_equivalent(12, 73))
    print(are_equivalent(12, 74))
    print(are_equivalent(1