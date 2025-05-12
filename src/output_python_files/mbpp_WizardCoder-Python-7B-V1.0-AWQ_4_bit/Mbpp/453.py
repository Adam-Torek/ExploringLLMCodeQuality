"""
Write a python function to find the sum of even factors of a number.
assert sumofFactors(18) == 26
"""

def sumofFactors(n):
    sum = 0
    for i in range(1, n+1):
        if n % i == 0 and i % 2 == 0:
            sum += i
    return sum

print(sumofFactors(18)) # Output: 26