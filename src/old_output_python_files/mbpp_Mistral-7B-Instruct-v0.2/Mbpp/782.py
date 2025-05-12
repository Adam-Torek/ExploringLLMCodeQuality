"""
Write a python function to find the sum of all odd length subarrays. https://www.geeksforgeeks.org/sum-of-all-odd-length-subarrays/
assert odd_length_sum([1,2,4]) == 14
"""
def odd_length_sum(arr):
    """
    :param arr: list of integers
    :return: sum of all odd length subarrays
    """
    n = len(arr)
    sum_odd_length = 0
    for i in range(1, n+1):
        sum_odd_length += sum(arr[j:j+i])
    return sum_odd_length

assert odd_length_sum([1,2,4]) == 14
assert odd_length_sum([1,2,3,4]) == 23
assert odd_length_sum([1,2,3,4,5]) == 41
assert odd_length_sum([1,2,3,4,5,6]) == 62
assert odd_length_sum([1,2,3,4,5,6,7]) == 85
assert odd_length_sum([1,2,3,4,5,6,7,8]) == 101
assert odd_length_sum([1,2,3,4,5,6,7,8,9]) == 119
assert odd_length_sum([1,2,3,4,5,6,7,8,9,10]) == 139
assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11]) == 161
assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12]) == 185
assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13]) == 209
assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14]) == 235
assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) == 263
assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]) == 293
assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]) == 325
assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]) == 359
assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]) == 395
assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]) == 433
assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]) == 473
assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]) == 515
assert odd_length_sum([1,2,3,4,