"""
Write a function to find sum and average of first n natural numbers.
assert sum_average(10)==(55, 5.5)
"""

def sum_average(n):
    total = sum(range(1, n+1))
    average = total/n
    return total, average

assert sum_average(10)==(55, 5.5)