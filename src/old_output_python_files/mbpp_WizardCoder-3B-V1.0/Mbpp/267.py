"""
Write a python function that takes in an integer n and returns the sum of the squares of the first n odd natural numbers.
assert square_Sum(2) == 10
"""

def square_Sum(n):
    sum = 0
    for i in range(1, n+1, 2):
        sum += i*i
    return sum

# Test the function
assert square_Sum(2) == 10<|endoftext|>