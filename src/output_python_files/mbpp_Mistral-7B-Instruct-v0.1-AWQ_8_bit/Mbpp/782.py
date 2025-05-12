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
        return sum([arr[i:i+2] for i in range(len(arr)-1)]) + odd_length_sum(arr[1:-1])


if __name__ == '__main__':
    assert odd_length_sum([1,2,4]) == 14
    assert odd_length_sum([1,2,3,4]) == 20
    assert odd_length_sum([1,2,3,4,5]) == 25
    assert odd_length_sum([1,2,3,4,5,6]) == 30
    assert odd_length_sum([1,2,3,4,5,6,7]) == 35
    assert odd_length_sum([1,2,3,4,5,6,7,8]) == 40
    assert odd_length_sum([1,2,3,4,5,6,7,8,9]) == 45
    assert odd_length_sum([1,2,3,4,5,6,7,8,9,10]) == 50
    assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11]) == 55
    assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12]) == 60
    assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13]) == 65
    assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14]) == 70
    assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) == 75
    assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]) == 80
    assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]) == 85
    assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]) == 90
    assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]) == 95
    assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]) == 100
    assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]) == 105
    assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,