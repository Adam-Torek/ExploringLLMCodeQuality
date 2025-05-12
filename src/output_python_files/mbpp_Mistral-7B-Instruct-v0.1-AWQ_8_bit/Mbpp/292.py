"""
Write a python function to find quotient of two numbers (rounded down to the nearest integer).
assert find(10,3) == 3
"""

def find(x,y):
    return round(x/y)

#test
assert find(10,3) == 3