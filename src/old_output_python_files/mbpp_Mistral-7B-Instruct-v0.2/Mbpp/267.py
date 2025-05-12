"""
Write a python function that takes in an integer n and returns the sum of the squares of the first n odd natural numbers.
assert square_Sum(2) == 10
"""
def square_sum(n):
    sum = 0
    i = 1
    while i <= n:
        if i % 2 != 0:
            sum += i * i
        i += 1
    return sum

assert square_sum(2) == 10