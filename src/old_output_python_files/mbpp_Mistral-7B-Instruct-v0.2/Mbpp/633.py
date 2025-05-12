"""
Write a python function to find the sum of xor of all pairs of numbers in the given list.
assert pair_xor_Sum([5,9,7,6],4) == 47
"""
def pair_xor_sum(numbers, expected_sum):
    """
    :param numbers: list of integers
    :param expected_sum: expected sum of xor of all pairs of numbers in the list
    :return: None if the sum is equal to expected_sum, otherwise raises an AssertionError
    """
    total_xor = 0
    n = len(numbers)
    for i in range(n):
        for j in range(i+1, n):
            xor = numbers[i] ^ numbers[j]
            total_xor += xor
    if total_xor == expected_sum:
        print("The sum of xor of all pairs of numbers in the list is: ", total_xor)
    else:
        raise AssertionError("The sum of xor of all pairs of numbers in the list is not equal to the expected sum: ", expected_sum)

pair_xor_sum([5,9,7,6], 47)