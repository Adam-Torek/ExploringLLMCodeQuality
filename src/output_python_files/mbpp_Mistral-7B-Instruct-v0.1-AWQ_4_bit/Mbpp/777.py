"""
Write a python function to find the sum of non-repeated elements in a given list.
assert find_sum([1,2,3,1,1,4,5,6]) == 21
"""

def find_sum(lst):
    """
    This function takes a list as an input and returns the sum of non-repeated elements in the list.
    """
    sum = 0
    for i in lst:
        if lst.count(i) == 1:
            sum += i
    return sum

# Test the function
assert find_sum([1,2,3,1,1,4,5,6]) == 21