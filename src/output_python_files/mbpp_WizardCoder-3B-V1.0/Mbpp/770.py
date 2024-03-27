"""
Write a python function to find the sum of fourth power of first n odd natural numbers.
assert odd_num_sum(2) == 82
"""

def odd_num_sum(n):
    return sum(x**4 for x in range(1, n+1, 2))

# Test the function
assert odd_num_sum(2) == 82<|endoftext|>