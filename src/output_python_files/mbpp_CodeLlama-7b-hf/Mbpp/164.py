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
    if a == b:
        return True
    if a < b:
        a, b = b, a
    divisors = []
    for i in range(1, a + 1):
        if a % i == 0:
            divisors.append(i)
    if sum(divisors) == b:
        return True
    return False


if __name__ == '__main__':
    print(are_equivalent(36, 57))
    print(are_equivalent(36, 54))
    print(are_equivalent(36, 55))
    print(are_equivalent(36, 56))
    print(are_equivalent(36, 58))
    print(are_equivalent(36, 59))
    print(are_equivalent(36, 60))
    print(are_equivalent(36, 61))
    print(are_equivalent(36, 62))
    print(are_equivalent(36, 63))
    print(are_equivalent(36, 64))
    print(are_equivalent(36, 65))
    print(are_equivalent(36, 66))
    print(are_equivalent(36, 67))
    print(are_equivalent(36, 68))
    print(are_equivalent(36, 69))
    print(are_equivalent(36, 70))
    print(are_equivalent(36, 71))
    print(are_equivalent(36, 72))
    print(are_equivalent(36, 73))
    print(are_equivalent(36, 74))
    print(are_equivalent(36, 75))
    print(are_equivalent(36, 76))
    print(are_equivalent(36, 77))
    print(are_equivalent(36, 78))
    print(are_equivalent(36, 79))
    print(are_equivalent(36, 80))
    print(are_equivalent(36, 81))
    print(are_equivalent(36, 82))
    print(are_equivalent(36, 83))
    print(are_equivalent(36, 84))
    print(are_equivalent(36, 85))
    print(are_equivalent(36, 86))
    print(are_equivalent(36, 87))
    print(are_equivalent(36, 88))
    print(are_equivalent(36, 89))
    print(are_equivalent(36, 90))
    print(are_equivalent(36, 91))
    print(are_equivalent(36, 92))
    print(are_equivalent(36, 93))
    print(are_equivalent(36, 94))
    print(are_equivalent(36, 95))
    print(are_equivalent(36, 96))
    print(are_equivalent(36, 97))
    print(are_equivalent(36, 98))
    print(are_equivalent(36, 99))
    print(are_equivalent(36, 100))
    print(are_equivalent(36, 101))
    print(are_equivalent(36, 102))
    print(are_equivalent(