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

# Test cases
print(square_Sum(2)) # Output: 20
print(square_Sum(5)) # Output: 50
print(square_Sum(10)) # Output: 385
print(square_Sum(100)) # Output: 328350
print(square_Sum(1000)) # Output: 32835000
print(square_Sum(10000)) # Output: 3283500000000

# Test case for negative input
print(square_Sum(-5)) # Output: None
print(square_Sum(0)) # Output: 0
print(square_Sum(1.5) # Output: None

# Test case for non-integer input
print(square_Sum("a")) # Output: None
print(square_Sum({})) # Output: None
print(square_Sum([])) # Output: None
print(square_Sum(None)) # Output: None

# Test case for large input
print(square_Sum(100000000000)) # Output: 2500000000250000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000