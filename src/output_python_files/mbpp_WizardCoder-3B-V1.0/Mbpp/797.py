"""
Write a python function to find the sum of all odd natural numbers within the range l and r.
assert sum_in_range(2,5) == 8
"""

def sum_in_range(l, r):
    return sum(x for x in range(l, r+1) if x % 2!= 0)

# Test the function
assert sum_in_range(2,5) == 8<|endoftext|>