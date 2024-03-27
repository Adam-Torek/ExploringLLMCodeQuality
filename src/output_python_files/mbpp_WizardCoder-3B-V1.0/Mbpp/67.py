"""
Write a function to find the number of ways to partition a set of Bell numbers.
assert bell_number(2)==2
"""

def bell_number(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return bell_number(n-1) + bell_number(n-2)

# Test the function
assert bell_number(2) == 2
assert bell_number(3) == 5
assert bell_number(4) == 10
assert bell_number(5) == 15<|endoftext|>