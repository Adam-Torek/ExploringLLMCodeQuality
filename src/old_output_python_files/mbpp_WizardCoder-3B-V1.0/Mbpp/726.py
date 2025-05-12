"""
Write a function that takes as input a tuple of numbers (t_1,...,t_{N+1}) and returns a tuple of length N where the i-th element of the tuple is equal to t_i * t_{i+1}.
assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
"""

def multiply_elements(t):
    return tuple(t[i] * t[i+1] for i in range(len(t)-1))

# Test the function with the given example
assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)<|endoftext|>