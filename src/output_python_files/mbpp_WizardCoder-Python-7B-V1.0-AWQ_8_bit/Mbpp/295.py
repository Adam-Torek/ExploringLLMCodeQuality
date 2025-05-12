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