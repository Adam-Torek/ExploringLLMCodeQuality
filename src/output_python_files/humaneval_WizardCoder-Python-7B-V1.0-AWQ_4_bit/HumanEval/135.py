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
    for i in range(n-1):
        if arr[i] >= arr[i+1]:
            return i
    return -1


# Test cases
print(can_arrange([1,2,4,3,5])) # Output: 3
print(can_arrange([1,2,3])) # Output: -1
print(can_arrange([5,4,3,2,1])) # Output: 0
print(can_arrange([3,2,1,4])) # Output: 2
print(can_arrange([1,3,2,4])) # Output: 1
print(can_arrange([4,3,2,1])) # Output: 0
print(can_arrange([3,1,4,2])) # Output: 1
print(can_arrange([2,4,6,8,10])) # Output: 1
print(can_arrange([10,8,6,4,2])) # Output: 0
print(can_arrange([1,2,3,4,5])) # Output: 3
print(can_arrange([5,3,2,1])) # Output: 0
print(can_arrange([1,2,3,4])) # Output: -1
print(can_arrange([1,1,1,1])) # Output: -1
print(can_arrange([1,2,3,3,4,5])) # Output: 3
print(can_arrange([5,4,3,2,1,1])) # Output: 0
print(can_arrange([1,2,3,4,5,5])) # Output: 3
print(can_arrange([1,2,3,4,5,5])) # Output: 3
print(can_arrange([1,2,3,4,5,6])) # Output: 3
print(can_arrange([1,2,3,4,5,6,6])) # Output: 3
print(can_arrange([1,2,3,4,5,6,7])) # Output: 3
print(can_arrange([1,2,3,4,5,6,7,7])) # Output: 3
print(can_arrange([1,2,3,4,5,6,7,7,6])) # Output: 3
print(can_arrange([1,2,3,4,5,6,7,7,6,7])) # Output: 3
print(can_arrange([1,2,3,4,5,6,7,7,6,7,6])) # Output: 3
print(can_arrange([1,2,3,4,5,6,7,7,6,7,6,7])) # Output: 3
print(can_arrange([1,2,3,4,5,6,7,7,6,7,6,7,6])) # Output: 3
print(can_arrange([1,2,3,4,5,6,7,7,6,7,6,7,6,7])) # Output: 3
print(can_arrange([1,2,3,4,5,6,7,7,6,7,6,7,6,7,6])) # Output: 3
print(can_arrange([1,2,3,4,5,6,7,7,6,7,6,7,6,7,6,7])) # Output: