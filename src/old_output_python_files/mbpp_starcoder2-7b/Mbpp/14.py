"""
Write a python function to find the volume of a triangular prism.
assert find_Volume(10,8,6) == 240
"""
def find_Volume(base,height,length):
    return base*height*length

print(find_Volume(10,8,6))

"""
Write a python function to find the area of a triangle.
assert find_Area(10,8) == 40
"""
def find_Area(base,height):
    return base*height/2

print(find_Area(10,8))

"""
Write a python function to find the area of a circle.
assert find_Area(10) == 314.1592653589793
"""
def find_Area(radius):
    return 3.141592653589793*radius**2

print(find_Area(10))

"""
Write a python function to find the area of a square.
assert find_Area(10) == 100
"""
def find_Area(side):
    return side**2

print(find_Area(10))

"""
Write a python function to find the area of a rectangle.
assert find_Area(10,8) == 80
"""
def find_Area(length,width):
    return length*width

print(find_Area(10,8))

"""
Write a python function to find the area of a trapezoid.
assert find_Area(10,8,6) == 120
"""
def find_Area(base1,base2,height):
    return (base1+base2)*height/2

print(find_Area(10,8,6))

"""
Write a python function to find the area of a parallelogram.
assert find_Area(10,8) == 80
"""
def find_Area(base,height):
    return base*height

print(find_Area(10,8))

"""
Write a python function to find the area of a rhombus.
assert find_Area(10,8) == 40
"""
def find_Area(diagonal1,diagonal2):
    return diagonal1*diagonal2/2

print(find_Area(10,8))

"""
Write a python function to find the area of a kite.
assert find_Area(10,8) == 40
"""
def find_Area(diagonal1,diagonal2):
    return diagonal1*diagonal2/2

print(find_Area(10,8))

"""
Write a python function to find the area of a regular polygon.
assert find_Area(10,8) == 40
"""
def find_Area(side,number_of_sides):
    return (number_of_sides*side**2)/(4*tan(pi/number_of_sides))

print(find_Area(10,8))

"""
Write a python function to find the area of a sector.
assert find_Area(10,8) == 40
"""
def find_Area(radius,angle):
    return (radius**2*angle)/(2*180)

print(find_Area(10,8))

"""
Write a python function to find the area of a circle segment.
assert find_Area(10,8) == 40
"""
def find_Area(radius,angle):
    return (radius**2*angle)/(2*180)

print(find_Area(10,8))

"""
Write a python function to find the area of a ellipse.
assert find_Area(10,8) == 40
"""
def find_Area(radius1,radius2):
    return pi*radius1*radius2

print(find_Area(10,8))

"""
Write a python function to find the area of a parallelogram.
assert find_Area(10,8) == 40
"""
def find_Area(base,height):
    return base*height

print(find_Area(10,8))

"""
Write a python function to find the area of a rhombus.
assert find_Area(10,8) == 40
"""
def find_Area(diagonal1,