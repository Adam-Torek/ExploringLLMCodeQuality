"""
Write a python function to find the number of numbers with an odd value when rotating a binary string the given number of times.
assert odd_Equivalent("011001",6) == 3
"""


def odd_Equivalent(binary_string, rotations):
    """
    :param binary_string: str
    :param rotations: int
    :return: int
    """
    if rotations == 0:
        return len(binary_string) - binary_string.count("0")
    else:
        return odd_Equivalent(binary_string[1:], rotations - 1) + binary_string[0]


if __name__ == '__main__':
    print(odd_Equivalent("011001", 6))
    print(odd_Equivalent("011001", 1))
    print(odd_Equivalent("011001", 0))
    print(odd_Equivalent("011001", 10))
    print(odd_Equivalent("011001", 100))
    print(odd_Equivalent("011001", 1000))
    print(odd_Equivalent("011001", 10000))
    print(odd_Equivalent("011001", 100000))
    print(odd_Equivalent("011001", 1000000))
    print(odd_Equivalent("011001", 10000000))
    print(odd_Equivalent("011001", 100000000))
    print(odd_Equivalent("011001", 1000000000))
    print(odd_Equivalent("011001", 10000000000))
    print(odd_Equivalent("011001", 100000000000))
    print(odd_Equivalent("011001", 1000000000000))
    print(odd_Equivalent("011001", 10000000000000))
    print(odd_Equivalent("011001", 100000000000000))
    print(odd_Equivalent("011001", 1000000000000000))
    print(odd_Equivalent("011001", 10000000000000000))
    print(odd_Equivalent("011001", 100000000000000000))
    print(odd_Equivalent("011001", 1000000000000000000))
    print(odd_Equivalent("011001", 10000000000000000000))
    print(odd_Equivalent("011001", 100000000000000000000))
    print(odd_Equivalent("011001", 1000000000000000000000))
    print(odd_Equivalent("011001", 10000000000000000000000))
    print(odd_Equivalent