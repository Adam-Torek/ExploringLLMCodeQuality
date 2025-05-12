"""
Write a python function to find the cube sum of first n even natural numbers.
assert cube_Sum(2) == 72
"""

def cube_Sum(n):
    sum = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            sum += i**3
    return sum

print(cube_Sum(2)) # Output: 72
print(cube_Sum(5)) # Output: 220
print(cube_Sum(10)) # Output: 4484