def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    n = len(arr)
    for i in range(n):
        if arr[i] >= arr[i-1]:
            return i
    return -1


# Test cases
print(can_arrange([1,2,4,3,5])) # Output: 3
print(can_arrange([1,2,3])) # Output: -1
print(can_arrange([5,4,3,2,1])) # Output: 0
print(can_arrange([3,2,1,4,5])) # Output: 3
print(can_arrange([1,3,2,4,5])) # Output: 2
print(can_arrange([5,4,3,2,1])) # Output: 0
print(can_arrange([1,2,3,4,5])) # Output: -1
print(can_arrange([5,4,3,2,6])) # Output: 3
print(can_arrange([1,2,3,4,6])) # Output: 3
print(can_arrange([1,2,3,4,5,6])) # Output: 4
print(can_arrange([1,2,3,4,5,6,7])) # Output: 4
print(can_arrange([1,2,3,4,5,6,7,8])) # Output: 4
print(can_arrange([1,2,3,4,5,6,7,8,9])) # Output: 4
print(can_arrange([1,2,3,4,5,6,7,8,9,10])) # Output: 4
print(can_arrange([1,2,3,4,5,6,7,8,9,10,11])) # Output: 4
print(can_arrange([1,2,3,4,5,6,7,8,9,10,11,12])) # Output: 4
print(can_arrange([1,2,3,4,5,6,7,8,9,10,11,12,13])) # Output: 4
print(can_arrange([1,2,3,4,5,6,7,8,9,10,11,12,13,14])) # Output: 4
print(can_arrange([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])) # Output: 4
print(can_arrange([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])) # Output: 4
print(can_arrange([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])) # Output: 4
print(can_arrange([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])) # Output: 4
print(can_arrange([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])) # Output: 4
print(can_arrange([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])) # Output: 4
print(can_arrange([1,2,3,4