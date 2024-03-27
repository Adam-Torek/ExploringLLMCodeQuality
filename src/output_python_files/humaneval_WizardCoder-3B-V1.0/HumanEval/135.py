def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

# Solution:
# We can solve this problem by iterating through the array and keeping track of
# the largest index of an element which is not greater than or equal to the
# element immediately preceding it. We can do this by keeping track of the
# largest index seen so far and comparing it to the current index. If the
# current index is greater than the largest index seen so far, we update the
# largest index seen so far.

# If we reach the end of the array without finding a suitable index, we return -1.

def can_arrange(arr):
    largest_index = -1
    for i in range(len(arr)):
        if arr[i] >= arr[i-1]:
            largest_index = i
            break
    return largest_index

# Test cases
print(can_arrange([1,2,4,3,5])) # Output: 3
print(can_arrange([1,2,3])) # Output: -1<|endoftext|>