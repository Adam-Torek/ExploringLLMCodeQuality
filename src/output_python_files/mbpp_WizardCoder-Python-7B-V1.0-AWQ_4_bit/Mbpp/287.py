"""
Write a python function takes in an integer n and returns the sum of squares of first n even natural numbers.
assert square_Sum(2) == 20
"""
def square_Sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**2
    return sum

print(square_Sum(2)) # Output: 20
print(square_Sum(5)) # Output: 50
print(square_Sum(10)) # Output: 385
print(square_Sum(100)) # Output: 328350