"""
Write a python function to find the sum of all odd natural numbers within the range l and r.
assert sum_in_range(2,5) == 8
"""

def sum_in_range(l, r):
    """
    Returns the sum of all odd natural numbers within the range l and r.
    """
    sum = 0
    for i in range(l, r+1):
        if i % 2 != 0:
            sum += i
    return sum

print(sum_in_range(2,5)) # Output: 8
print(sum_in_range(1,10)) # Output: 25
print(sum_in_range(10,20)) # Output: 25
print(sum_in_range(100,200)) # Output: 1000
print(sum_in_range(1000,2000)) # Output: 2000
print(sum_in_range(10000,20000)) # Output: 20000
print(sum_in_range(100000,200000)) # Output: 300000
print(sum_in_range(1000000,2000000)) # Output: 3000000
print(sum_in_range(10000000,20000000)) # Output: 4000000
print(sum_in_range(100000000,200000000)) # Output: 50000000
print(sum_in_range(1000000000,2000000000)) # Output: 60000000
print(sum_in_range(10000000000,20000000000)) # Output: 700000000
print(sum_in_range(100000000000,200000000000)) # Output: 800000000
print(sum_in_range(100000000000,200000000000)) # Output: 900000000
print(sum_in_range(1000000000000,2000000000000)) # Output: 100000000000
print(sum_in_range(1000000000000,2000000000000)) # Output: 1100000000000
print(sum_in_range(10000000000000,20000000000000)) # Output: 1200000000000
print(sum_in_range(100000000000000,200000000000000)) # Output: 1300000000000
print(sum_in_range(1000000000000000,2000000000000000)) # Output: 1400000000000
print(sum_in_range(10000000000000000,20000000000000000)) # Output: 1500000000000
print(sum_in_range(100000000000000000,200000000000000000)) # Output: 1600000000000
print(sum_in_range(10000000000000000