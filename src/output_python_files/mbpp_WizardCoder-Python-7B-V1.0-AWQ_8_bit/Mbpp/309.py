"""
Write a python function to find the maximum of two numbers.
assert maximum(5,10) == 10
"""
def maximum(a,b):
    if a>b:
        return a
    else:
        return b

print(maximum(5,10)) # Output: 10
print(maximum(10,5)) # Output: 10
print(maximum(10,10)) # Output: 10
print(maximum(-5,0)) # Output: 0
print(maximum(-10,-15)) # Output: -5
print(maximum(0,-5)) # Output: 0

# Test cases
# print(maximum(10,5)) # Output: 10
# print(maximum(-5,10)) # Output: 10
# print(maximum(-10,-5)) # Output: -5
# print(maximum(0,0)) # Output: 0
# print(maximum(5,5)) # Output: 5
# print(maximum(-5,-10)) # Output: -5
# print(maximum(100,200)) # Output: 200
# print(maximum(-100,-200)) # Output: -100
# print(maximum(-5,5)) # Output: 5
# print(maximum(0,100) # Output: 100
# print(maximum(-10,-20) # Output: -10
# print(maximum(100,-200) # Output: -20
# print(maximum(-200,100) # Output: -20
# print(maximum(0,-100) # Output: -100
# print(maximum(-10,10) # Output: 10
# print(maximum(10,-10) # Output: 10
# print(maximum(-5,-5) # Output: -5
# print(maximum(0,0) # Output: 0
# print(maximum(-10,0) # Output: 0
# print(maximum(0,-10) # Output: 0
# print(maximum(-5,5) # Output: 5
# print(maximum(5,5) # Output: 5
# print(maximum(-5,-5) # Output: -5
# print(maximum(10,10) # Output: 10
# print(maximum(-10,-10) # Output: -10
# print(maximum(0,0) # Output: 0
# print(maximum(-10,0) # Output: 0
# print(maximum(0,-10) # Output: 0
# print(maximum(5,10) # Output: 10
# print(maximum(10,5) # Output: 10
# print(maximum(-5,-10) # Output: -5
# print(maximum(-10,-5) # Output: -5
# print(maximum(0,0) # Output: 0
# print(maximum(-5,0) # Output: 0
# print(maximum(10,0) # Output: 10
# print(maximum(-10,0) # Output: 0
# print(maximum(0,-5) # Output: 0
# print(maximum(-5,-10) # Output: -5
# print(maximum(0,10) # Output: 10
# print(maximum(-10,5) # Output: 5
# print(maximum(-5,10) # Output: 10
# print(maximum(10,-5) # Output: 10
# print(maximum(5,-10) # Output: -5
# print(maximum(-5,0) # Output: 0
# print(maximum(0,-5) # Output: 0
# print(maximum(-10,0) # Output: 0
# print(maximum(5,0) # Output: 5
# print(maximum(-5,0) # Output: 0
# print(maximum(0,-5) # Output: 0
# print