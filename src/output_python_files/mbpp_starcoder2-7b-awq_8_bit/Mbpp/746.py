"""
Write a function to find area of a sector. The function takes the radius and angle as inputs. Function should return None if the angle is larger than 360 degrees.
assert sector_area(4,45)==6.283185307179586
"""

def sector_area(radius, angle):
    if angle > 360:
        return None
    else:
        return (radius**2)*angle/360

assert sector_area(4,45)==6.283185307179586

"""
Write a function to find the area of a triangle. The function takes the length of the base and height as inputs.
assert triangle_area(4,4)==8
"""

def triangle_area(base, height):
    return (base*height)/2

assert triangle_area(4,4)==8

"""
Write a function to find the area of a circle. The function takes the radius as input.
assert circle_area(4)==50.26548245743669
"""

def circle_area(radius):
    return 3.141592653589793*radius**2

assert circle_area(4)==50.26548245743669

"""
Write a function to find the area of a rectangle. The function takes the length and width as inputs.
assert rectangle_area(4,4)==16
"""

def rectangle_area(length, width):
    return length*width

assert rectangle_area(4,4)==16

"""
Write a function to find the area of a square. The function takes the length of the side as input.
assert square_area(4)==16
"""

def square_area(side):
    return side**2

assert square_area(4)==16

"""
Write a function to find the area of a parallelogram. The function takes the base and height as inputs.
assert parallelogram_area(4,4)==16
"""

def parallelogram_area(base, height):
    return base*height

assert parallelogram_area(4,4)==16

"""
Write a function to find the area of a trapezoid. The function takes the length of the base1, base2 and height as inputs.
assert trapezoid_area(4,4,4)==16
"""

def trapezoid_area(base1, base2, height):
    return ((base1+base2)/2)*height

assert trapezoid_area(4,4,4)==16

"""
Write a function to find the area of a triangle. The function takes the length of the base and height as inputs.
assert triangle_area(4,4)==8
"""

def triangle_area(base, height):
    return (base*height)/2

assert triangle_area(4,4)==8

"""
Write a function to find the area of a circle. The function takes the radius as input.
assert circle_area(4)==50.26548245743669
"""

def circle_area(radius):
    return 3.141592653589793*radius**2

assert circle_area(4)==50.26548245743669

"""
Write a function to find the area of a rectangle. The function takes the length and width as inputs.
assert rectangle_area(4,4)==16
"""

def rectangle_area(length, width):
    return length*width

assert rectangle_area(4,4)==16

"""
Write a function to find the area of a square. The function takes the length of the side as input.
assert square_area(4)==16
"""

def square_area(side):
    return side**2

assert square_area(4)==16

"""
Write a function to find the area of a parallelogram. The function takes the base and height as inputs.
assert parallelogram_area(4,4)==16
"""

def parallelogram_area(base, height):
    return base*height

assert parallelogram_area(4,4)==16

"""
Write a function to find the area