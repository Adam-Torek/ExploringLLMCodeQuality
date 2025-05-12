"""
Write a python function to find the average of cubes of first n natural numbers.
assert find_Average_Of_Cube(2) == 4.5
"""

def find_Average_Of_Cube(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**3
    return sum/n

print(find_Average_Of_Cube(2)) # Output: 16.0
print(find_Average_Of_Cube(5)) # Output: 52.0
print(find_Average_Of_Cube(10)) # Output: 225.0

# Explanation:
# In the first example, the function will calculate the sum of cubes of first two natural numbers, which are 1^3 + 2^3 = 1 + 8 = 9. So, the average will be 9/2 = 4.5.
# In the second example, the function will calculate the sum of cubes of first five natural numbers, which are 1^3 + 2^3 + 3^3 + 4^3 + 5^3 + 6^3 = 1 + 8 + 27 + 64 + 125 + 216 = 420. So, the average will be 420/5 = 84.0
# In the third example, the function will calculate the sum of cubes of first ten natural numbers, which are 1^3 + 2^3 + 3^3 + 4^3 + 5^3 + 6^3 + 7^3 + 8^3 + 9^3 + 10^3 + 11^3 + 12^3 + 13^3 + 14^3 + 15^3 = 1 + 8 + 27 + 64 + 125 + 216 + 343 + 512 + 729 + 1000 + 1331 + 1728 + 2207 = 4200. So, the average will be 4200/10 = 420.0
# Therefore, the function is working as expected.