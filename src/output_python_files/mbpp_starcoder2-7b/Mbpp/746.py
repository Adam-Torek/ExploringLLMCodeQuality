"""
Write a function to find area of a sector. The function takes the radius and angle as inputs. Function should return None if the angle is larger than 360 degrees.
assert sector_area(4,45)==6.283185307179586
"""

def sector_area(radius, angle):
    if angle > 360:
        return None
    else:
        return (radius**2)*angle*0.01591549430918956

print(sector_area(4,45))

"""
Write a function to find the area of a triangle. The function takes the length of the base and height as inputs.
assert triangle_area(4,4)==8
"""

def triangle_area(base, height):
    return (base*height)*0.5

print(triangle_area(4,4))

"""
Write a function to find the area of a circle. The function takes the radius as input.
assert circle_area(4)==50.26548245743669
"""

def circle_area(radius):
    return (radius**2)*3.141592653589793

print(circle_area(4))

"""
Write a function to find the area of a rectangle. The function takes the length and width as inputs.
assert rectangle_area(4,4)==16
"""

def rectangle_area(length, width):
    return length*width

print(rectangle_area(4,4))

"""
Write a function to find the area of a square. The function takes the length of the side as input.
assert square_area(4)==16
"""

def square_area(side):
    return side**2

print(square_area(4))

"""
Write a function to find the area of a trapezoid. The function takes the length of the parallel sides and the height as inputs.
assert trapezoid_area(4,4,4)==16
"""

def trapezoid_area(parallel_side1, parallel_side2, height):
    return (parallel_side1+parallel_side2)*height*0.5

print(trapezoid_area(4,4,4))

"""
Write a function to find the area of a parallelogram. The function takes the length of the base and height as inputs.
assert parallelogram_area(4,4)==16
"""

def parallelogram_area(base, height):
    return base*height

print(parallelogram_area(4,4))

"""
Write a function to find the area of a rhombus. The function takes the length of the diagonal and the height as inputs.
assert rhombus_area(4,4)==16
"""

def rhombus_area(diagonal, height):
    return (diagonal*height)*0.5

print(rhombus_area(4,4))

"""
Write a function to find the area of a kite. The function takes the length of the diagonal and the height as inputs.
assert kite_area(4,4)==16
"""

def kite_area(diagonal1, diagonal2):
    return (diagonal1*diagonal2)*0.5

print(kite_area(4,4))

"""
Write a function to find the area of a regular polygon. The function takes the length of the side and the number of sides as inputs.
assert regular_polygon_area(4,4)==16
"""

def regular_polygon_area(side, number_of_sides):
    return (number_of_sides*side**2)*0.5

print(regular_polygon_area(4,4))

"""
Write a function to find the area of a regular hexagon. The function takes the length of the side as input.
assert hexagon_area(4)==16
"""

def hexagon_area(side):
    return (3*side**2)*0.5

print(hexagon_area(4))

"""
Write a function to find the area of a regular octagon. The function takes the length of the side as input.
assert octagon_area(4)==16
"""

def octagon_area(side):
    return (2*(1+2**0.5)*side**2)*