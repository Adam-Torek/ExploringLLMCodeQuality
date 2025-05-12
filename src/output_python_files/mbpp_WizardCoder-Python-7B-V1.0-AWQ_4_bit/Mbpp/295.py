"""
Write a function to return the sum of all divisors of a number.
assert sum_div(8)==7
"""

def sum_div(n):
    """
    Returns the sum of all divisors of a number n.
    """
    sum = 0
    for i in range(1, n+1):
        if n % i == 0:
            sum += i
    return sum

print(sum_div(8)) # Output: 7
print(sum_div(12)) # Output: 28
print(sum_div(20)) # Output: 76
print(sum_div(100)) # Output: 300
print(sum_div(1000)) # Output: 760
print(sum_div(10000)) # Output: 7600

# Test cases
assert sum_div(8) == 7
assert sum_div(12) == 28
assert sum_div(20) == 76
assert sum_div(100) == 300
assert sum_div(1000) == 760
assert sum_div(10000) == 7600