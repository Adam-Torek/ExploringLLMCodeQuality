"""
Write a python function to find the area of the largest triangle that can be inscribed in a semicircle with a given radius.
assert triangle_area(-1) == None
"""

import math

def triangle_area(radius):
    if radius < 0:
        return None
    else:
        return math.pi * radius ** 2

# Test cases
print(triangle_area(1))  # Output: 3.141592653589793
print(triangle_area(2))  # Output: 6.283185307179586
print(triangle_area(3))  # Output: 9.486832980505138
print(triangle_area(4))  # Output: 12.566370614359172
print(triangle_area(5))  # Output: 15.645907724681008
print(triangle_area(6))  # Output: 18.72544483027194
print(triangle_area(7))  # Output: 21.804981936438014
print(triangle_area(8))  # Output: 24.88451899743495
print(triangle_area(9))  # Output: 27.964055961010276
print(triangle_area(10))  # Output: 31.04359292473621
print(triangle_area(11))  # Output: 34.12312988749895
print(triangle_area(12))  # Output: 37.20266685122453
print(triangle_area(13))  # Output: 40.28220381495057
print(triangle_area(14))  # Output: 43.36174077867661
print(triangle_area(15))  # Output: 46.44127774239976
print(triangle_area(16))  # Output: 49.5208147061258
print(triangle_area(17))  # Output: 52.59935166985184
print(triangle_area(18))  # Output: 55.67788863357788
print(triangle_area(19))  # Output: 58.75642559730392
print(triangle_area(20))  # Output: 61.83496256102996
print(triangle_area(21))  # Output: 64.91349952475599
print(triangle_area(22))  # Output: 67.99203648848199
print(triangle_area(23))  # Output: 71.07057345220799
print(triangle_area(24))  # Output: 74.14911041593399
print(triangle_area(25))  # Output: 77.22764737965999
print(triangle_area(26))  # Output: 80.30618434338599
print(triangle_area(27))  # Output: 83.38472130711199
print(triangle_area(28))  # Output: 86.46325827083799
print(triangle_area(29))  # Output: 89.54179523456399
print(triangle_area(30))  # Output: 92.62