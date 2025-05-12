"""
Write a python function to find the sum of xor of all pairs of numbers in the given list.
assert pair_xor_Sum([5,9,7,6],4) == 47
"""
def pair_xor_Sum(lst, target):
    """
    :param lst: list of integers
    :param target: integer
    :return: sum of xor of all pairs of numbers in the given list
    """
    if not lst:
        return 0
    n = len(lst)
    sum = 0
    for i in range(n):
        for j in range(i+1, n):
            sum += lst[i] ^ lst[j]
    return sum == target


if __name__ == '__main__':
    assert pair_xor_Sum([5,9,7,6],4) == 47
    assert pair_xor_Sum([1,2,3,4],10) == 45
    assert pair_xor_Sum([1,2,3,4],15) == 0
    assert pair_xor_Sum([1,2,3,4],20) == 0
    assert pair_xor_Sum([1,2,3,4],25) == 0