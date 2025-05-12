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
    for i in range(n):
        sum_odd_length += arr[i]
        if i < n-1:
            sum_odd_length += sum(arr[i+1:i+len(arr)+1])
    return sum_odd_length

if __name__ == "__main__":
    assert odd_length_sum([1,2,4]) == 14
    assert odd_length_sum([1,2,3,4]) == 22
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
    assert odd_length_sum([1,2,3,4,5,6,7,8,9,10,1