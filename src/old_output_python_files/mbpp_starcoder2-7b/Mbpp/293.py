"""
Write a function to find the third side of a right angled triangle.
assert otherside_rightangle(7,8)==10.63014581273465
"""
def otherside_rightangle(a,b):
    return (a**2+b**2)**0.5

"""
Write a function to find the area of a right angled triangle.
assert area_rightangle(7,8)==24.0
"""
def area_rightangle(a,b):
    return 0.5*a*b

"""
Write a function to find the perimeter of a right angled triangle.
assert perimeter_rightangle(7,8)==22.0
"""
def perimeter_rightangle(a,b):
    return a+b+otherside_rightangle(a,b)

"""
Write a function to find the hypotenuse of a right angled triangle.
assert hypotenuse_rightangle(7,8)==11.0
"""
def hypotenuse_rightangle(a,b):
    return otherside_rightangle(a,b)

"""
Write a function to find the height of a right angled triangle.
assert height_rightangle(7,8)==5.0
"""
def height_rightangle(a,b):
    return a*b/(otherside_rightangle(a,b))

"""
Write a function to find the area of a triangle.
assert area_triangle(7,8,9)==16.0
"""
def area_triangle(a,b,c):
    s=(a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5

"""
Write a function to find the perimeter of a triangle.
assert perimeter_triangle(7,8,9)==22.0
"""
def perimeter_triangle(a,b,c):
    return a+b+c

"""
Write a function to find the semiperimeter of a triangle.
assert semiperimeter_triangle(7,8,9)==13.0
"""
def semiperimeter_triangle(a,b,c):
    return (a+b+c)/2

"""
Write a function to find the height of a triangle.
assert height_triangle(7,8,9)==5.0
"""
def height_triangle(a,b,c):
    return (a*b*c)/(4*area_triangle(a,b,c))

"""
Write a function to find the base of a triangle.
assert base_triangle(7,8,9)==7.0
"""
def base_triangle(a,b,c):
    return (a**2+b**2-c**2)/(2*b)

"""
Write a function to find the area of a trapezium.
assert area_trapezium(7,8,9,10)==30.0
"""
def area_trapezium(a,b,c,d):
    return 0.5*(a+b)*c

"""
Write a function to find the perimeter of a trapezium.
assert perimeter_trapezium(7,8,9,10)==24.0
"""
def perimeter_trapezium(a,b,c,d):
    return a+b+c+d

"""
Write a function to find the height of a trapezium.
assert height_trapezium(7,8,9,10)==5.0
"""
def height_trapezium(a,b,c,d):
    return (a+b-c-d)/2

"""
Write a function to find the area of a parallelogram.
assert area_parallelogram(7,8,9,10)==56.0
"""
def area_parallelogram(a,b,c,d):
    return a*b

"""
Write a function to find the perimeter of a parallelogram.
assert perimeter_parallelogram(7,8,9,10)==30.0
"""
def perimeter_parallelogram(a,b,c,d):
    return 2*(a+b)

"""
Write a function to find the height of a parallelogram.
assert height_parallelogram(7,8,9,10)==5