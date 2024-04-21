"""
Write a function to that rotate left bits by d bits a given number. We assume that the number is 32 bit.
assert left_rotate(16,2) == 64
"""

def left_rotate(num, d):
    """
    Rotate left bits by d bits a given number.
    """
    return (num << d) | (num >> (32 - d))

# Test cases
print(left_rotate(16,2)) # Output: 64<|endoftext|>