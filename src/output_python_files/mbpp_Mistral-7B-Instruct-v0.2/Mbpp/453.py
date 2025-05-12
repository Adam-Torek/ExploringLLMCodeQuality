"""
Write a python function to find the sum of even factors of a number.
assert sumofFactors(18) == 26
"""
def sumofFactors(n):
    sum = 0
    i = 1
    while i <= n:
        if n % i == 0 and i % 2 == 0:
            sum += i
        i += 1
    return sum

assert sumofFactors(18) == 26