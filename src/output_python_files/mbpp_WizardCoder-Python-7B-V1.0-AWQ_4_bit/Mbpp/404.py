"""
Write a python function to find the minimum of two numbers.
assert minimum(1,2) == 1
"""

def minimum(a, b):
    if a < b:
        return a
    else:
        return b

print(minimum(1,2)) # Output: 1
print(minimum(2,1)) # Output: 1
print(minimum(3,3)) # Output: 3
print(minimum(-1,4)) # Output: -1
print(minimum(-5,-6)) # Output: -6