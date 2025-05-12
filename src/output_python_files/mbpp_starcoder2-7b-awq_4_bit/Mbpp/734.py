"""
Write a python function to find sum of products of all possible sublists of a given list. https://www.geeksforgeeks.org/sum-of-products-of-all-possible-subarrays/
assert sum_Of_Subarray_Prod([1,2,3]) == 20
"""

def sum_Of_Subarray_Prod(arr):
    pass

def test_sum_Of_Subarray_Prod():
    assert sum_Of_Subarray_Prod([1,2,3]) == 20
    assert sum_Of_Subarray_Prod([1,2,3,4]) == 140
    assert sum_Of_Subarray_Prod([1,2,3,4,5]) == 350
    assert sum_Of_Subarray_Prod([1,2,3,4,5,6]) == 1320
    assert sum_Of_Subarray_Prod([1,2,3,4,5,6,7]) == 6300
    assert sum_Of_Subarray_Prod([1,2,3,4,5,6,7,8]) == 33600
    assert sum_Of_Subarray_Prod([1,2,3,4,5,6,7,8,9]) == 198400
    assert sum_Of_Subarray_Prod([1,2,3,4,5,6,7,8,9,10]) == 1197520
    assert sum_Of_Subarray_Prod([1,2,3,4,5,6,7,8,9,10,11]) == 7175760
    assert sum_Of_Subarray_Prod([1,2,3,4,5,6,7,8,9,10,11,12]) == 40824960
    assert sum_Of_Subarray_Prod([1,2,3,4,5,6,7,8,9,10,11,12,13]) == 235411320
    assert sum_Of_Subarray_Prod([1,2,3,4,5,6,7,8,9,10,11,12,13,14]) == 1372108840
    assert sum_Of_Subarray_Prod([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) == 8469046000
    assert sum_Of_Subarray_Prod([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]) == 51891847936
    assert sum_Of_Subarray_Prod([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]) == 314666222080
    assert sum_Of_Subarray_Prod([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]) == 1911029860096
    assert sum_Of_Subarray_Prod([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]) == 11979399936768
    assert sum_Of_Subarray_Prod([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]) == 71757600000000
    assert sum_Of_Subarray_Prod([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]) == 4