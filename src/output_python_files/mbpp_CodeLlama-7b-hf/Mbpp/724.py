"""
Write a function that takes base and power as arguments and calculate the sum of all digits of the base to the specified power.
assert power_base_sum(2,100)==115
"""


def power_base_sum(base, power):
    """
    :param base: int
    :param power: int
    :return: int
    """
    if power == 0:
        return 0
    if power == 1:
        return base
    if power == 2:
        return base * base
    if power == 3:
        return base * base * base
    if power == 4:
        return base * base * base * base
    if power == 5:
        return base * base * base * base * base
    if power == 6:
        return base * base * base * base * base * base
    if power == 7:
        return base * base * base * base * base * base * base
    if power == 8:
        return base * base * base * base * base * base * base * base
    if power == 9:
        return base * base * base * base * base * base * base * base * base
    if power == 10:
        return base * base * base * base * base * base * base * base * base * base
    if power == 11:
        return base * base * base * base * base * base * base * base * base * base * base
    if power == 12:
        return base * base * base * base * base * base * base * base * base * base * base * base
    if power == 13:
        return base * base * base * base * base * base * base * base * base * base * base * base * base
    if power == 14:
        return base * base * base * base * base * base * base * base * base * base * base * base * base * base
    if power == 15:
        return base * base * base * base * base * base * base * base * base * base * base * base * base * base * base
    if power == 16:
        return base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base
    if power == 17:
        return base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base
    if power == 18:
        return base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base
    if power == 19:
        return base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base
    if power == 20:
        return base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base
    if power == 21:
        return base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base
    if power == 22:
        return base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base
    if power == 23:
        return base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base * base
    if power == 24:
        return base * base * base * base * base * base *