"""
Write a python function to find the product of the array multiplication modulo n.
assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9
"""


def find_remainder(arr, n):
    """
    :param arr: list of integers
    :param n: integer
    :return: integer
    """
    if not arr:
        return 0
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return (arr[0] * arr[1]) % n
    if len(arr) == 3:
        return (arr[0] * arr[1] * arr[2]) % n
    if len(arr) == 4:
        return (arr[0] * arr[1] * arr[2] * arr[3]) % n
    if len(arr) == 5:
        return (arr[0] * arr[1] * arr[2] * arr[3] * arr[4]) % n
    if len(arr) == 6:
        return (arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5]) % n
    if len(arr) == 7:
        return (arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6]) % n
    if len(arr) == 8:
        return (arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6] * arr[7]) % n
    if len(arr) == 9:
        return (arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6] * arr[7] * arr[8]) % n
    if len(arr) == 10:
        return (arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6] * arr[7] * arr[8] * arr[9]) % n
    if len(arr) == 11:
        return (arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6] * arr[7] * arr[8] * arr[9] * arr[10]) % n
    if len(arr) == 12:
        return (arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6] * arr[7] * arr[8] * arr[9] * arr[10] * arr[11]) % n
    if len(arr) == 13:
        return (arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6] * arr[7] * arr[8] * arr[9] * arr[10] * arr[11] * arr[12]) % n
    if len(arr) == 14:
        return (arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6] * arr[7] * arr[8] * arr[9] * arr[10] * arr[11] * arr[12] * arr[13]) % n
    if len(arr) == 15:
        return (arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6] * arr[7] * arr[8] * arr[9] * arr[10] * arr[11] * arr[12] * arr[13] * arr[14]) % n
    if len(arr) == 16:
        return (arr[0] * arr[1] * arr[2] * arr[3] * arr[4] * arr[5] * arr[6] * arr[7