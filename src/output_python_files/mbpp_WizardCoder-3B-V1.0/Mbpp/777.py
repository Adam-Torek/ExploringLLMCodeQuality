"""
Write a python function to find the sum of non-repeated elements in a given list.
assert find_sum([1,2,3,1,1,4,5,6]) == 21
"""

def find_sum(lst):
    # create a set to store unique elements
    unique_set = set(lst)
    # calculate the sum of unique elements
    unique_sum = sum(unique_set)
    # return the sum of non-repeated elements
    return unique_sum

# test the function
assert find_sum([1,2,3,1,1,4,5,6]) == 21<|endoftext|>