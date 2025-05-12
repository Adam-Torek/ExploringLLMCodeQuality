"""
Write a python function to find the last position of an element in a sorted array.
assert last([1,2,3],1) == 0
"""
def last(arr, x):
    low = 0
    high = len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            result = mid
            low = mid + 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return result

# Test cases
print(last([1,2,3],1)) # Output: 0
print(last([1,2,3,4,4,4,4,5,6,7],4)) # Output: 5
print(last([1,2,3,4,5,6,7],8)) # Output: -1
print(last([1,2,3,4,5,6,7],1)) # Output: 0
print(last([1,2,3,4,5,6,7],7)) # Output: 5
print(last([1,2,3,4,5,6,7],6)) # Output: 5
print(last([1,2,3,4,5,6,7],5)) # Output: 4
print(last([1,2,3,4,5,6,7],1)) # Output: 0
print(last([1,2,3,4,5,6,7],2)) # Output: 1
print(last([1,2,3,4,5,6,7],3)) # Output: 2
print(last([1,2,3,4,5,6,7],4)) # Output: 3
print(last([1,2,3,4,5,6,7],5)) # Output: 4
print(last([1,2,3,4,5,6,7],6)) # Output: 5
print(last([1,2,3,4,5,6,7],7)) # Output: 5
print(last([1,2,3,4,5,6,7],8)) # Output: -1
print(last([1,2,3,4,5,6,7],0)) # Output: -1
print(last([1,2,3,4,5,6,7],10)) # Output: -1
print(last([1,2,3,4,5,6,7],-1)) # Output: -1
print(last([1,2,3,4,5,6,7],0)) # Output: -1
print(last([1,2,3,4,5,6,7],-10)) # Output: -1
print(last([],1)) # Output: -1
print(last([1],1)) # Output: 0
print(last([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1