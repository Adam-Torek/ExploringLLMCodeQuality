"""
Write a function to find the sum of numbers in a list within a range specified by two indices.
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
"""

def sum_range_list(lst, start, end):
    """
    This function takes in a list and two indices and returns the sum of the numbers in the list
    between the start and end indices.
    """
    if start > end:
        return "Invalid indices"
    else:
        sum = 0
        for i in range(start, end+1):
            sum += lst[i]
        return sum

# test the function
assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29