"""
Write a python function to count minimum number of swaps required to convert one binary number represented as a string to another.
assert min_Swaps("1101","1110") == 1
"""


def min_Swaps(str1, str2):
    """
    :param str1: string
    :param str2: string
    :return: int
    """
    if len(str1) != len(str2):
        raise ValueError("Strings must be of equal length")

    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1

    return count


if __name__ == "__main__":
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1010", "1100"))
    print(min_Swaps("1101", "1010"))
    print(min_Swaps("1110", "1101"))
    print(min_Swaps("1010", "1001"))
    print(min_Swaps("1110", "1101"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps("1101", "1110"))
    print(min_Swaps