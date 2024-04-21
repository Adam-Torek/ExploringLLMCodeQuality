"""
Write a python function to remove odd numbers from a given list.
assert remove_odd([1,2,3]) == [2]
"""

def remove_odd(lst):
    return [x for x in lst if x % 2 == 0]

# Test the function
print(remove_odd([1,2,3])) # Output: [2]<|endoftext|>