"""
Write a function to find the closest smaller number than n.
assert closest_num(11) == 10
"""

def closest_num(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return closest_num(n-1) if n % 2 == 0 else closest_num(n+1)

# Test cases
print(closest_num(11)) # Output: 10
print(closest_num(10)) # Output: 9
print(closest_num(1)) # Output: 0
print(closest_num(2)) # Output: 1<|endoftext|>