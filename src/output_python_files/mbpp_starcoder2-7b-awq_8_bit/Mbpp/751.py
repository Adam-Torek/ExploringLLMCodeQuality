"""
Write a function to check if the given array represents min heap or not. https://www.geeksforgeeks.org/how-to-check-if-a-given-array-represents-a-binary-heap/
assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
"""

def check_min_heap(arr):
    for i in range(len(arr)):
        if 2*i+1 < len(arr) and arr[2*i+1] < arr[i]:
            return False
        if 2*i+2 < len(arr) and arr[2*i+2] < arr[i]:
            return False
    return True

assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
assert check_min_heap([1, 2, 3, 4, 5, 6, 7]) == False
assert check_min_heap([1, 2, 3, 4, 5, 6, 7, 8]) == False
assert check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9]) == False
assert check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
assert check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == False
assert check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == False
assert check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == False
assert check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == False
assert check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == False
assert check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == False
assert check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == False
assert check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]) == False
assert check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == False
assert check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == False
assert check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19