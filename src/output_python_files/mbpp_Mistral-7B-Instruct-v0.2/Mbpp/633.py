"""
Write a python function to find the sum of xor of all pairs of numbers in the given list.
assert pair_xor_Sum([5,9,7,6],4) == 47
"""
def pair_xor_sum(numbers, expected_sum):
    """
    :param numbers: list of integers
    :param expected_sum: expected sum of xor of all pairs of numbers in the list
    :return: boolean value indicating if the sum of xor of all pairs of numbers in the list is equal to the expected sum
    """
    total_xor = 0
    n = len(numbers)
    for i in range(n):
        for j in range(i+1, n):
            xor = numbers[i] ^ numbers[j]
            total_xor += xor
    return total_xor == expected_sum

assert pair_xor_sum([5,9,7,6], 47) == True
assert pair_xor_sum([1,2,3,4], 6) == False