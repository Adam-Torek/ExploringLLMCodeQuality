"""
Write a function to find the third side of a right angled triangle.
assert otherside_rightangle(7,8)==10.63014581273465
"""

def otherside_rightangle(a,b):
    c = a**2 + b**2
    return (a**2 + b**2)**0.5

print(otherside_rightangle(7,8))<|endoftext|>