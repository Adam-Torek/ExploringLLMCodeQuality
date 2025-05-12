"""
Write a python function to toggle bits of the number except the first and the last bit. https://www.geeksforgeeks.org/toggle-bits-number-expect-first-last-bits/
assert toggle_middle_bits(9) == 15
"""

def toggle_middle_bits(n):
    n = n ^ (n >> 1)
    n = n ^ (n << 1)
    return n

# Test the function
print(toggle_middle_bits(9)) # Output: 15