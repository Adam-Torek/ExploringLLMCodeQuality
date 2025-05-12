"""
Write a function to find the sum of numbers in a list within a range specified by two indices.
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
"""

def sum_range_list(lst, start, end):
    """
    Returns the sum of numbers in a list within a range specified by two indices.
    """
    return sum(lst[start:end+1])

# Test the function
print(sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10)) # Output: 29