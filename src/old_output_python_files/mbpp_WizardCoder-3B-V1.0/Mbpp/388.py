"""
Write a python function to find the highest power of 2 that is less than or equal to n.
assert highest_Power_of_2(10) == 8
"""

def highest_Power_of_2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 2 ** (n.bit_length() - 1)

# Test the function
assert highest_Power_of_2(10) == 8<|endoftext|>