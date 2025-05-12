"""
Write a python function to find the difference between largest and smallest value in a given list.
assert big_diff([1,2,3,4]) == 3
"""

def big_diff(lst):
    return max(lst) - min(lst)

# Test the function
print(big_diff([1,2,3,4])) # Output: 3<|endoftext|>