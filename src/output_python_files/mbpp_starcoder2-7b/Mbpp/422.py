"""
Write a python function to find the average of cubes of first n natural numbers.
assert find_Average_Of_Cube(2) == 4.5
"""
def find_Average_Of_Cube(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i**3
    return sum/n

print(find_Average_Of_Cube(2))
/python_basics/python_basics_1.py
"""
Write a python function to find the sum of cubes of first n natural numbers.
assert find_Sum_Of_Cube(2) == 14
"""
def find_Sum_Of_Cube(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i**3
    return sum

print(find_Sum_Of_Cube(2))
/python_basics/python_basics_3.py
"""
Write a python function to find the sum of squares of first n natural numbers.
assert find_Sum_Of_Square(2) == 5
"""
def find_Sum_Of_Square(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i**2
    return sum

print(find_Sum_Of_Square(2))
/python_basics/python_basics_2.py
"""
Write a python function to find the average of squares of first n natural numbers.
assert find_Average_Of_Square(2) == 3.5
"""
def find_Average_Of_Square(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i**2
    return sum/n

print(find_Average_Of_Square(2))