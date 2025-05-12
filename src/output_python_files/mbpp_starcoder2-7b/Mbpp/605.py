"""
Write a function to check if the given integer is a prime number.
assert prime_num(13)==True
"""

def prime_num(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

print(prime_num(13))
/02_python_basics/03_functions/01_functions.py
"""
Write a function to calculate the area of a triangle.
assert area_of_triangle(3,4,5)==6
"""

def area_of_triangle(a,b,c):
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    return area

print(area_of_triangle(3,4,5))
/02_python_basics/02_conditionals/02_conditionals.py
"""
Write a function to check if the given number is even or odd.
assert even_odd(10)==True
"""

def even_odd(n):
    if n%2==0:
        return True
    else:
        return False

print(even_odd(10))
/02_python_basics/03_functions/02_functions.py
"""
Write a function to calculate the area of a rectangle.
assert area_of_rectangle(3,4)==12
"""

def area_of_rectangle(a,b):
    area=a*b
    return area

print(area_of_rectangle(3,4))
/02_python_basics/03_functions/03_functions.py
"""
Write a function to calculate the area of a circle.
assert area_of_circle(3)==28.274333882308138
"""

def area_of_circle(r):
    area=3.14*r*r
    return area

print(area_of_circle(3))
/02_python_basics/03_functions/04_functions.py
"""
Write a function to calculate the area of a square.
assert area_of_square(3)==9
"""

def area_of_square(a):
    area=a*a
    return area

print(area_of_square(3))
/02_python_basics/03_functions/05_functions.py
"""
Write a function to calculate the area of a trapezoid.
assert area_of_trapezoid(3,4,5)==10
"""

def area_of_trapezoid(a,b,h):
    area=0.5*(a+b)*h
    return area

print(area_of_trapezoid(3,4,5))
/02_python_basics/03_functions/06_functions.py
"""
Write a function to calculate the area of a parallelogram.
assert area_of_parallelogram(3,4,5)==6
"""

def area_of_parallelogram(a,b,h):
    area=a*b
    return area

print(area_of_parallelogram(3,4,5))
/02_python_basics/03_functions/07_functions.py
"""
Write a function to calculate the area of a rhombus.
assert area_of_rhombus(3,4,5)==6
"""

def area_of_rhombus(a,b,h):
    area=0.5*a*b
    return area

print(area_of_rhombus(3,4,5))
/02_python_basics/03_functions/08_functions.py
"""
Write a function to calculate the area of a regular polygon.
assert area_of_regular_polygon(3,4,5)==6
"""

def area_of_regular_polygon(n,a,h):
    area=0.5*n*a*h
    return area

print(area_of_regular_polygon(3,4,5))
/02_python_basics/03_functions/09_functions.py
"""