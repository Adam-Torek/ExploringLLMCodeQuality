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
    else:
        return sum(int(i) for i in str(base ** power))


if __name__ == '__main__':
    print(power_base_sum(2, 100))
    print(power_base_sum(2, 1000))
    print(power_base_sum(2, 10000))
    print(power_base_sum(2, 100000))
    print(power_base_sum(2, 1000000))
    print(power_base_sum(2, 10000000))
    print(power_base_sum(2, 100000000))
    print(power_base_sum(2, 1000000000))
    print(power_base_sum(2, 10000000000))
    print(power_base_sum(2, 100000000000))
    print(power_base_sum(2, 1000000000000))
    print(power_base_sum(2, 10000000000000))
    print(power_base_sum(2, 100000000000000))
    print(power_base_sum(2, 1000000000000000))
    print(power_base_sum(2, 10000000000000000))
    print(power_base_sum(2, 100000000000000000))
    print(power_base_sum(2, 1000000000000000000))
    print(power_base_sum(2, 10000000000000000000))
    print(power_base_sum(2, 100000000000000000000))
    print(power_base_sum(2, 1000000000000000000000))
    print(power_base_sum(2, 10000000000000000000000))
    print(power_base_sum(2, 100000000000000000000000))
    print(power_base_sum(2, 1000000000000000000000000))
    print(power_base_sum(2, 10000000000000000000000000))
    print(power_base_sum(2, 100000000000000000000000000))
    print(power_base_sum(2, 1000000000000000000000000000))
    print(power_base_sum(2, 10000000000000000000000000000))
    print(power_base_sum(2, 100000000000000000000000000000))
    print(power_base_sum(2, 10000000000000000000