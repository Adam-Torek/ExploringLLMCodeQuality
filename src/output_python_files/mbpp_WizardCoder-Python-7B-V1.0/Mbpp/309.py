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
print(maximum(-5,10) # Output: 10
print(maximum(-5,-10) # Output: -5