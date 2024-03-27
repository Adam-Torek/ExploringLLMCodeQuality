"""
Write a python function to find the average of cubes of first n natural numbers.
assert find_Average_Of_Cube(2) == 4.5
"""
def find_Average_Of_Cube(n):
    sum = 0
    for i in range(1,n+1):
        sum += i**3
    average = sum / n
    return average

assert find_Average_Of_Cube(2) == 4.5</s>