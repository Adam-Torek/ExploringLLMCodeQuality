"""
Write a python function to find the sum of common divisors of two given numbers.
assert sum(10,15) == 6
"""


def sum(a, b):
    """
    :param a: int
    :param b: int
    :return: int
    """
    if a < b:
        a, b = b, a
    result = 0
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            result += i
    return result


if __name__ == '__main__':
    print(sum(10, 15))
    print(sum(10, 10))
    print(sum(10, 5))
    print(sum(10, 2))
    print(sum(10, 1))
    print(sum(10, 0))
    print(sum(10, -1))
    print(sum(10, -10))
    print(sum(10, -15))
    print(sum(10, -20))
    print(sum(10, -25))
    print(sum(10, -30))
    print(sum(10, -35))
    print(sum(10, -40))
    print(sum(10, -45))
    print(sum(10, -50))
    print(sum(10, -55))
    print(sum(10, -60))
    print(sum(10, -65))
    print(sum(10, -70))
    print(sum(10, -75))
    print(sum(10, -80))
    print(sum(10, -85))
    print(sum(10, -90))
    print(sum(10, -95))
    print(sum(10, -100))
    print(sum(10, -105))
    print(sum(10, -110))
    print(sum(10, -115))
    print(sum(10, -120))
    print(sum(10, -125))
    print(sum(10, -130))
    print(sum(10, -135))
    print(sum(10, -140))
    print(sum(10, -145))
    print(sum(10, -150))
    print(sum(10, -155))
    print(sum(10, -160))
    print(sum(10, -165))
    print(sum(10, -170))
    print(sum(10, -175))
    print(sum(10, -180))
    print(sum(10, -185))
    print(sum(10, -190))
    print(sum(10, -195))
    print(sum(10, -200))
    print(sum(10, -205))
    print(sum(10, -210))
    print(sum(10, -215))
    print(sum(10, -220))
    print(sum(10, -225))
    print(sum(10, -230))
    print(sum(10, -235))
    print(sum(10, -240))
    print(sum(10, -245))
    print(sum(10, -250))
    print(sum(10, -255))
    print(sum(10, -260))
    print(sum(10, -265))
    print(sum(10, -270))
    print(sum(10, -275))
    print(sum(10, -280))
    print(sum(10, -2