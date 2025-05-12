"""
Write a function to check if the given array represents min heap or not. https://www.geeksforgeeks.org/how-to-check-if-a-given-array-represents-a-binary-heap/
assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
"""

def check_min_heap(arr):
    n = len(arr)
    for i in range(n//2):
        if arr[i] > arr[2*i+1] or arr[i] > arr[2*i+2]:
            return False
        if 2*i+2 < n and arr[2*i+1] > arr[2*i+2]:
            return False
    return True

# Test cases
print(check_min_heap([1, 2, 3, 4, 5, 6])) # True
print(check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # False
print(check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) # False
print(check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])) # True
print(check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])) # False
print(check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) # False
print(check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) # False
print(check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])) # False
print(check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])) # False
print(check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])) # False
print(check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])) # False
print(check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) # False
print(check_min_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20