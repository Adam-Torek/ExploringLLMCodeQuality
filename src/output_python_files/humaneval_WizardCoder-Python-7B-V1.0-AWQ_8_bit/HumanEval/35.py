def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    max_num = l[0]
    for i in l:
        if i > max_num:
            max_num = i
    return max_num


# Test cases
print(max_element([1, 2, 3])) # Output: 3
print(max_element([5, 3, -5, 2, -3, 9, 0, 123, 1, -10])) # Output: 123


# Time complexity: O(n)
# Space complexity: O(1)

# Can be optimized by using a variable to keep track of the current maximum element found, instead of looping through the entire list.

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 9, 0, 123, 1, -10])
    123
    """
    max_num = l[0]
    current_max = l[0]
    for i in l:
        if i > current_max:
            max_num = i
            current_max = i
    return max_num

# Test cases
print(max_element([1, 2, 3])) # Output: 3
print(max_element([5, 3, -5, 2, -3, 9, 0, 123, 1, -10])) # Output: 123

# Time complexity: O(n)
# Space complexity: O(1)

# Can be further optimized by using a variable to keep track of the current maximum element found, instead of looping through the entire list.

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 9, 0, 123, 1, -10])
    123
    """
    current_max = l[0]
    for i in l:
        if i > current_max:
            current_max = i
    return current_max

# Test cases
print(max_element([1, 2, 3])) # Output: 3
print(max_element([5, 3, -5, 2, -3, 9, 0, 123, 1, -10])) # Output: 123

# Time complexity: O(n)
# Space complexity: O(1)

# This implementation uses a variable to keep track of the current maximum element found, instead of looping through the entire list.