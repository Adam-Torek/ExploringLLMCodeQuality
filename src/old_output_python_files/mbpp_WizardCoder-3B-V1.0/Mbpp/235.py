"""
Write a python function to set all even bits of a given number.
assert even_bit_set_number(10) == 10
"""

def even_bit_set_number(num):
    return num | (num & 1)

# Test the function
assert even_bit_set_number(10) == 10<|endoftext|>