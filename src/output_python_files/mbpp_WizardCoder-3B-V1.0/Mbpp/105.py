"""
Write a python function to count true booleans in the given list.
assert count([True,False,True]) == 2
"""
def count(lst):
    count = 0
    for i in lst:
        if i:
            count += 1
    return count

# Test the function
assert count([True,False,True]) == 2<|endoftext|>