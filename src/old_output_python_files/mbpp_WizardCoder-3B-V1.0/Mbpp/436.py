"""
Write a python function to return the negative numbers in a list.
assert neg_nos([-1,4,5,-6]) == [-1,-6]
"""
def neg_nos(lst):
    return [x for x in lst if x < 0]

# Test the function
print(neg_nos([-1,4,5,-6])) # Output: [-1, -6]<|endoftext|>