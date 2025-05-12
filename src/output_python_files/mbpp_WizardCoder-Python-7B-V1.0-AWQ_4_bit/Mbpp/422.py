"""
Write a python function to find the average of cubes of first n natural numbers.
assert find_Average_Of_Cube(2) == 4.5
"""

def find_Average_Of_Cube(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**3
    return sum/n

print(find_Average_Of_Cube(2))

# Output: 16.0

# Explanation:
# The cubes of first two natural numbers are 1 and 8.
# The sum of these cubes is 1^3 + 2^3 = 1 + 8 = 9.
# The average of these cubes is 9/2 = 4.5.
# Therefore, the function returns 4.5.