"""
Write a python function to find the number of numbers with an odd value when rotating a binary string the given number of times.
assert odd_Equivalent("011001",6) == 3
"""


def odd_Equivalent(binary_string, rotations):
    """
    :param binary_string: string
    :param rotations: int
    :return: int
    """
    if not binary_string:
        return 0
    if rotations == 0:
        return 1
    if len(binary_string) == 1:
        return 1
    if len(binary_string) == 2:
        return 1 if binary_string[0] == binary_string[1] else 2
    if len(binary_string) == 3:
        return 1 if binary_string[0] == binary_string[2] else 2
    if len(binary_string) == 4:
        return 1 if binary_string[0] == binary_string[3] else 2
    if len(binary_string) == 5:
        return 1 if binary_string[0] == binary_string[4] else 2
    if len(binary_string) == 6:
        return 1 if binary_string[0] == binary_string[5] else 2
    if len(binary_string) == 7:
        return 1 if binary_string[0] == binary_string[6] else 2
    if len(binary_string) == 8:
        return 1 if binary_string[0] == binary_string[7] else 2
    if len(binary_string) == 9:
        return 1 if binary_string[0] == binary_string[8] else 2
    if len(binary_string) == 10:
        return 1 if binary_string[0] == binary_string[9] else 2
    if len(binary_string) == 11:
        return 1 if binary_string[0] == binary_string[10] else 2
    if len(binary_string) == 12:
        return 1 if binary_string[0] == binary_string[11] else 2
    if len(binary_string) == 13:
        return 1 if binary_string[0] == binary_string[12] else 2
    if len(binary_string) == 14:
        return 1 if binary_string[0] == binary_string[13] else 2
    if len(binary_string) == 15:
        return 1 if binary_string[0] == binary_string[14] else 2
    if len(binary_string) == 16:
        return 1 if binary_string[0] == binary_string[15] else 2
    if len(binary_string) == 17:
        return 1 if binary_string[0] == binary_string[16] else 2
    if len(binary_string) == 18:
        return 1 if binary_string[0] == binary_string[17] else 2
    if len(binary_string) == 19:
        return 1 if binary_string[0] == binary_string[18] else 2
    if len(binary_string) == 20:
        return 1 if binary_string[0] == binary_string[19] else 2
    if len(binary_string) == 21:
        return 1 if binary_string[0] == binary_string[20] else 2
    if len(binary_string) == 22:
        return 1 if binary_string[0] == binary_string[21] else 2
    if