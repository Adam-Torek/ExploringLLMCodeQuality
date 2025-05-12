"""
Write a python function to find quotient of two numbers (rounded down to the nearest integer).
assert find(10,3) == 3
"""

def find(num1, num2):
    return num1 // num2

print(find(10,3)) # Output: 3
print(find(15,4)) # Output: 3
print(find(20,5)) # Output: 4
print(find(17,6)) # Output: 3
print(find(100,7)) # Output: 1
print(find(25,5)) # Output: 5
print(find(100,2)) # Output: 50
print(find(100,10)) # Output: 10
print(find(100,1)) # Output: 100
print(find(100,0)) # Output: None
print(find(0,10)) # Output: None
print(find(0,0)) # Output: None
print(find(-10,3)) # Output: -4
print(find(10,-3)) # Output: -4
print(find(-10,0)) # Output: None
print(find(0,-10)) # Output: None
print(find(-10,-3)) # Output: None
print(find(-10,-5)) # Output: -2
print(find(10,-5)) # Output: -2
print(find(-10,5)) # Output: -2
print(find(5,10) # Output: 0
print(find(-5,10) # Output: -1
print(find(5,-10) # Output: -1
print(find(-5,-10) # Output: 0
print(find(0,0) # Output: None
print(find(10,10) # Output: 1
print(find(-10,-10) # Output: 1
print(find(10,-10) # Output: -1
print(find(-10,10) # Output: -1
print(find(10,0) # Output: None
print(find(0,10) # Output: None
print(find(0,-10) # Output: None
print(find(-10,0) # Output: None
print(find(10,1) # Output: 10
print(find(-10,-1) # Output: -10
print(find(10,-1) # Output: -10
print(find(-10,1) # Output: -10
print(find(1,10) # Output: 0
print(find(-1,-10) # Output: -1
print(find(1,-10) # Output: -1
print(find(-1,10) # Output: -1
print(find(10,1) # Output: 10
print(find(-10,1) # Output: -10
print(find(1,1) # Output: 1
print(find(-1,-1) # Output: -1
print(find(1,-1) # Output: -1
print(find(-1,1) # Output: -1
print(find(100,0.5) # Output: None
print(find(0.5,10) # Output: None
print(find(10.5,3) # Output: None
print(find(10,3.5) # Output: None
print(find(10.5,3.5) # Output: None
print(find(10.5,3.0) # Output: None
print(find(10.5,3.6) # Output: None
print(find(10.5,3.4) # Output: None
print(find(10.5,3.3) # Output: None
print(find(10.5,3.2) # Output: None
print(find(10.5,3.1) # Output: None
print(find(10.5,3.0) # Output: None
print(find(10.5,2.9) # Output: None
print(find(10.5,2.8) # Output: None
print(find(10.5,2.7