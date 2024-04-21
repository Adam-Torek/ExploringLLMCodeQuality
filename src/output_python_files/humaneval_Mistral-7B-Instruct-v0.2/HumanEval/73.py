def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    # First, we need to find the number of unique elements in the array
    unique_elements = set(arr)
    num_unique = len(unique_elements)

    # If the number of unique elements is odd, then we cannot make the array palindromic
    if num_unique % 2 == 1:
        return -1

    # Otherwise, we need to change half of the elements to make the array palindromic
    num_changes = num_unique // 2

    return num_changes

# Test cases
print(smallest_change([1,2,3,5,4,7,9,6])) # 4
print(smallest_change([1, 2, 3, 4, 3, 2, 2])) # 1
print(smallest_change([1, 2, 3, 2, 1])) # 0
print(smallest_change([1, 2, 3, 5, 4, 7, 9, 6, 6])) # 3
print(smallest_change([1, 2, 3, 5, 5, 4, 7, 9, 6, 6])) # 2
print(smallest_change([1, 2, 3, 5, 5, 5, 4, 7, 9, 6, 6])) # 1
print(smallest_change([1, 2, 3, 5, 5, 5, 5, 4, 7, 9, 6, 6])) # 0
print(smallest_change([1, 2, 3, 5, 5, 5, 5, 5, 4, 7, 9, 6, 6])) # -1</s>