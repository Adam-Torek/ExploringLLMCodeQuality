"""
Write a function to return the sum of all divisors of a number.
assert sum_div(8)==7
"""

def sum_div(n):
    sum = 1
    for i in range(2, n+1):
        if n%i == 0:
            sum += i
    return sum

assert sum_div(8)==7