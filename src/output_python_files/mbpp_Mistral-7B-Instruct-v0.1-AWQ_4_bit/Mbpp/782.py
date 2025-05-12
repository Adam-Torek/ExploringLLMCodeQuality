"""
Write a python function to find the sum of all odd length subarrays. https://www.geeksforgeeks.org/sum-of-all-odd-length-subarrays/
assert odd_length_sum([1,2,4]) == 14
"""

def odd_length_sum(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return arr[0] + arr[1]
    else:
        return sum([arr[i:i+2] for i in range(0, len(arr), 2)]) + odd_length_sum(arr[1:-1])


if __name__ == '__main__':
    assert odd_length_sum([1,2,4]) == 14
    assert odd_length_sum([1,2,3,4,5]) == 21
    assert odd_length_sum([1,2,3,4,5,6,7,8,9]) == 36
    assert odd_length_sum([1,2,3,4,5,6,7,8,9,10]) == 45
    assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11]) == 54
    assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12]) == 63
    assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13]) == 72
    assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14]) == 81
    assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) == 90
    assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]) == 99
    assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]) == 108
    assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]) == 117
    assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]) == 126
    assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]) == 135
    assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]) == 144
    assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,1