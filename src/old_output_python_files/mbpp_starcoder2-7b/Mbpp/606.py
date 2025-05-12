"""
Write a function to convert degrees to radians.
assert radian_degree(90)==1.5707963267948966
"""

def radian_degree(degree):
    return degree*math.pi/180

print(radian_degree(90))<file_sep>/python_basics/python_basics_1.py
"""
Write a function to calculate the area of a triangle.
assert area_triangle(3,4,5)==6
"""

def area_triangle(a,b,c):
    s=(a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5

print(area_triangle(3,4,5))<file_sep>/python_basics/python_basics_10.py
"""
Write a function to calculate the area of a circle.
assert area_circle(3)==28.274333882308138
"""

def area_circle(r):
    return 3.14*r*r

print(area_circle(3))<file_sep>/python_basics/python_basics_11.py
"""
Write a function to calculate the area of a rectangle.
assert area_rectangle(3,4)==12
"""

def area_rectangle(l,b):
    return l*b

print(area_rectangle(3,4))<file_sep>/python_basics/python_basics_12.py
"""
Write a function to calculate the area of a square.
assert area_square(3)==9
"""

def area_square(a):
    return a*a

print(area_square(3))<file_sep>/python_basics/python_basics_13.py
"""
Write a function to calculate the area of a trapezoid.
assert area_trapezoid(3,4,5)==10
"""

def area_trapezoid(a,b,h):
    return 0.5*(a+b)*h

print(area_trapezoid(3,4,5))<file_sep>/python_basics/python_basics_14.py
"""
Write a function to calculate the area of a parallelogram.
assert area_parallelogram(3,4)==12
"""

def area_parallelogram(b,h):
    return b*h

print(area_parallelogram(3,4))<file_sep>/python_basics/python_basics_15.py
"""
Write a function to calculate the area of a rhombus.
assert area_rhombus(3,4)==6
"""

def area_rhombus(d1,d2):
    return 0.5*d1*d2

print(area_rhombus(3,4))<file_sep>/python_basics/python_basics_16.py
"""
Write a function to calculate the area of a kite.
assert area_kite(3,4)==6
"""

def area_kite(d1,d2):
    return 0.5*d1*d2

print(area_kite(3,4))<file_sep>/python_basics/python_basics_17.py
"""
Write a function to calculate the area of a regular polygon.
assert area_regular_polygon(3,4)==6
"""

def area_regular_polygon(n,s):
    return (n*s**2)/(4*math.tan(math.pi/n))

print(area_regular_polygon(3,4))<file_sep>/python_basics/python_basics_18.py
"""
Write a function to calculate the area of a sector.
assert area_sector(3,4)==6
"""

def area_sector(r,a):
    return (a*r**2)/2

print(area_sector(3,4))<file_sep>/python_basics/python_basics_19.py
"""
Write a function to calculate the area of a circle segment.
assert area_circle_segment(3,4)==6
"""

def area_circle_segment(r,a):
    return (a*r**2)/360

print(area_circle_segment(3,4))<file_sep>/python_basics/python_basics_2.py
"""
Write a function to calculate the area of a square.
assert area_square(3)==9
"""