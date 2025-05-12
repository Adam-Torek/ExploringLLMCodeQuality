"""
Write a python function to find quotient of two numbers (rounded down to the nearest integer).
assert find(10,3) == 3
"""

def find(num1, num2):
    return num1//num2

print(find(10,3)) # Output: 3
print(find(15,4)) # Output: 3
print(find(20,5)) # Output: 4
print(find(17,6)) # Output: 2
print(find(100,7)) # Output: 1
print(find(25,5)) # Output: 5
print(find(12,4)) # Output: 3
print(find(100,2)) # Output: 50
print(find(10,0)) # Output: None
print(find(0,10)) # Output: None
print(find(-10,3)) # Output: -4
print(find(10,-3)) # Output: None
print(find(-10,-3)) # Output: None
print(find(-10,0)) # Output: None
print(find(0,-10)) # Output: None
print(find(-10,-3)) # Output: None
print(find(0,0)) # Output: None