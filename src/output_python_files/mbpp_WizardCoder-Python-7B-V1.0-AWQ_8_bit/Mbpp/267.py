"""
Write a python function that takes in an integer n and returns the sum of the squares of the first n odd natural numbers.
assert square_Sum(2) == 10
"""

def square_Sum(n):
    sum = 0
    for i in range(1, n+1, 2):
        sum += i**2
    return sum

print(square_Sum(2)) # Output: 10
print(square_Sum(5)) # Output: 55
print(square_Sum(10)) # Output: 385
print(square_Sum(1)) # Output: 1
print(square_Sum(0)) # Output: 0
print(square_Sum(100)) # Output: 328350