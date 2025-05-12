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

# Can be optimized using a single loop to find the maximum element in the list

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 9, 0, 123, 1, -10])
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

# Can be optimized using a single loop to find the maximum element in the list

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 9, 0, 123, 1, -10])
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

# Using a variable to store the current maximum element

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 9, 0, 123, 1, -10])
    123
    """
    max_num = l[0]
    for i in l:
        if i > max_num:
            max_num = i
    return max_