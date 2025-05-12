"""
Write a python function to find the next perfect square greater than a given number.
assert next_Perfect_Square(35) == 36
"""

def next_Perfect_Square(num):
    """
    This function takes a number as input and returns the next perfect square greater than the given number.
    """
    # Find the square root of the given number
    sqrt_num = int(num ** 0.5) + 1

    # Check if the square root is a perfect square
    if sqrt_num ** 2 == num:
        return sqrt_num

    # If the square root is not a perfect square, find the next perfect square greater than the square root
    else:
        return sqrt_num ** 2

# Test the function
print(next_Perfect_Square(35)) # Output: 36<|endoftext|>