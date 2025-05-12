"""
Write a function to calculate the value of 'a' to the power 'b'.
assert power(3,4) == 81
"""

def power(a, b):
    result = 1
    for i in range(b):
        result *= a
    return result

assert power(3,4) == 81<|endoftext|>