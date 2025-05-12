"""
Write a python function to find the cube sum of first n even natural numbers.
assert cube_Sum(2) == 72
"""

def cube_Sum(n):
    return (n * (n + 1) * (2 * n + 1)) // 6

# Test the function
assert cube_Sum(2) == 72<|endoftext|>