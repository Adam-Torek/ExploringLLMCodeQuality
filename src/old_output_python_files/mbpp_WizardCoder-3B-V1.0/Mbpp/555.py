"""
Write a python function to find the difference between the sum of cubes of the first n natural numbers and the sum of the first n natural numbers.
assert difference(3) == 30
"""

def difference(n):
    return (n * (n + 1) * (2 * n + 1)) - sum(range(1, n + 1))

# Test the function
assert difference(3) == 30<|endoftext|>