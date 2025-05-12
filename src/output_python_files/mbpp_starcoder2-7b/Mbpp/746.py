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
Write a function to find the area of a triangle. The function takes the length of the three sides as inputs. Function should return None if the sum of any two sides is less than the third side.
assert triangle_area(3,4,5)==6
"""

def triangle_area(a,b,c):
    if a+b<c or b+c<a or a+c<b:
        return None
    else:
        s=(a+b+c)/2
        return (s*(s-a)*(s-b)*(s-c))**0.5

print(triangle_area(3,4,5))

"""
Write a function to find the area of a parallelogram. The function takes the base and height as inputs. Function should return None if the base is less than 0 or the height is less than 0.
assert parallelogram_area(4,5)==20
"""

def parallelogram_area(base,height):
    if base<0 or height<0:
        return None
    else:
        return base*height

print(parallelogram_area(4,5))

"""
Write a function to find the area of a trapezoid. The function takes the length of the two parallel sides and the height as inputs. Function should return None if the length of any side is less than 0 or the height is less than 0.
assert trapezoid_area(4,5,6)==16
"""

def trapezoid_area(a,b,h):
    if a<0 or b<0 or h<0:
        return None
    else:
        return (a+b)*h/2

print(trapezoid_area(4,5,6))

"""
Write a function to find the area of a circle. The function takes the radius as input. Function should return None if the radius is less than 0.
assert circle_area(4)==50.26548245743669
"""

def circle_area(radius):
    if radius<0:
        return None
    else:
        return 3.14*radius**2

print(circle_area(4))

"""
Write a function to find the area of a rectangle. The function takes the length and width as inputs. Function should return None if the length or width is less than 0.
assert rectangle_area(4,5)==20
"""

def rectangle_area(length,width):
    if length<0 or width<0:
        return None
    else:
        return length*width

print(rectangle_area(4,5))

"""
Write a function to find the area of a rhombus. The function takes the length of the side as input. Function should return None if the length is less than 0.
assert rhombus_area(4)==16
"""

def rhombus_area(side):
    if side<0:
        return None
    else:
        return side**2

print(rhombus_area(4))

"""
Write a function to find the area of a square. The function takes the length of the side as input. Function should return None if the length is less than 0.
assert square_area(4)==16
"""

def square_area(side):
    if side<0:
        return None
    else:
        return side**2

print(square_area(4))

"""
Write a function to find the area of a kite. The function takes the length of the two diagonals as inputs. Function should return None if the length of any diagonal is less than 0.
assert kite_area(4,5)==1