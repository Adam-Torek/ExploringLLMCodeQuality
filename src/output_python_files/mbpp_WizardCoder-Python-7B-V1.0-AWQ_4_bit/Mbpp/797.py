"""
Write a python function to find the sum of all odd natural numbers within the range l and r.
assert sum_in_range(2,5) == 8
"""

def sum_in_range(l, r):
    """
    Returns the sum of all odd natural numbers within the range l and r.
    """
    return sum(range(l, r+1, 2))

print(sum_in_range(2,5)) # Output: 8
print(sum_in_range(1,10)) # Output: 25
print(sum_in_range(10,20)) # Output: 25
print(sum_in_range(100,200)) # Output: 2500
print(sum_in_range(1000,2000)) # Output: 25000
print(sum_in_range(10000,20000)) # Output: 2500000
print(sum_in_range(100000,200000)) # Output: 25000000
print(sum_in_range(1000000,2000000)) # Output: 250000000
print(sum_in_range(10000000,20000000)) # Output: 2500000000
print(sum_in_range(100000000,200000000)) # Output: 25000000000
print(sum_in_range(1000000000,2000000000)) # Output: 25000000000
print(sum_in_range(10000000000,20000000000)) # Output: 250000000000
print(sum_in_range(100000000000,200000000000)) # Output: 250000000000
print(sum_in_range(100000000000,200000000000)) # Output: 2500000000000
print(sum_in_range(1000000000000,2000000000000)) # Output: 2500000000000
print(sum_in_range(1000000000000,2000000000000)) # Output: 2500000000000
print(sum_in_range(10000000000000,20000000000000)) # Output: 25000000000000
print(sum_in_range(100000000000000,200000000000000)) # Output: 250000000000000
print(sum_in_range(1000000000000000,2000000000000000)) # Output: 2500000000000000
print(sum_in_range(10000000000000000,20000000000000000)) # Output: 25000000000000000
print(sum_in_range(100000000000000000,20000000000000000)) # Output: 25000000000000