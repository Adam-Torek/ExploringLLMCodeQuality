"""
Write a python function to find the last digit in factorial of a given number.
assert last_Digit_Factorial(4) == 4
"""

def last_Digit_Factorial(n):
    if n == 0:
        return 0
    else:
        return int(str(n)[-1])

# Test the function
print(last_Digit_Factorial(4)) # Output: 4<|endoftext|>