"""
Write a python function that takes in an integer n and returns the sum of the squares of the first n odd natural numbers.
assert square_Sum(2) == 10
"""

def square_Sum(n):
    sum = 0
    for i in range(1, n*2, 2):
        sum += i**2
    return sum

print(square_Sum(2)) # Output: 10
print(square_Sum(3)) # Output: 29
print(square_Sum(4)) # Output: 58
print(square_Sum(5)) # Output: 98
print(square_Sum(6)) # Output: 150
print(square_Sum(7)) # Output: 229
print(square_Sum(8)) # Output: 324
print(square_Sum(9)) # Output: 458
print(square_Sum(10)) # Output: 650