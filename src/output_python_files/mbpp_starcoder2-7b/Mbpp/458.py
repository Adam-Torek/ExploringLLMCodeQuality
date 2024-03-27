"""
Write a function to find the area of a rectangle.
assert rectangle_area(10,20)==200
"""
def rectangle_area(length,width):
    return length*width

print(rectangle_area(10,20))

"""
Write a function to find the area of a circle.
assert circle_area(10)==314.1592653589793
"""
def circle_area(radius):
    return 3.14*radius**2

print(circle_area(10))

"""
Write a function to find the area of a triangle.
assert triangle_area(10,20)==100
"""
def triangle_area(base,height):
    return 0.5*base*height

print(triangle_area(10,20))

"""
Write a function to find the area of a trapezoid.
assert trapezoid_area(10,20,30)==150
"""
def trapezoid_area(base1,base2,height):
    return 0.5*(base1+base2)*height

print(trapezoid_area(10,20,30))

"""
Write a function to find the area of a parallelogram.
assert parallelogram_area(10,20)==200
"""
def parallelogram_area(base,height):
    return base*height

print(parallelogram_area(10,20))

"""
Write a function to find the area of a rhombus.
assert rhombus_area(10,20)==200
"""
def rhombus_area(diagonal1,diagonal2):
    return 0.5*diagonal1*diagonal2

print(rhombus_area(10,20))

"""
Write a function to find the area of a square.
assert square_area(10)==100
"""
def square_area(side):
    return side**2

print(square_area(10))

"""
Write a function to find the area of a kite.
assert kite_area(10,20)==100
"""
def kite_area(diagonal1,diagonal2):
    return 0.5*diagonal1*diagonal2

print(kite_area(10,20))

"""
Write a function to find the area of a pentagon.
assert pentagon_area(10)==523.6
"""
def pentagon_area(side):
    return 1.732*side**2

print(pentagon_area(10))

"""
Write a function to find the area of a hexagon.
assert hexagon_area(10)==608.66
"""
def hexagon_area(side):
    return 2*side**2

print(hexagon_area(10))

"""
Write a function to find the area of a heptagon.
assert heptagon_area(10)==785.714
"""
def heptagon_area(side):
    return 2.618*side**2

print(heptagon_area(10))

"""
Write a function to find the area of an octagon.
assert octagon_area(10)==926.1
"""
def octagon_area(side):
    return 2*(1+2.414213562373095*0.5)*side**2

print(octagon_area(10))

"""
Write a function to find the area of a nonagon.
assert nonagon_area(10)==1131.034
"""
def nonagon_area(side):
    return 2*(1+2*0.5773502691896257)*side**2

print(nonagon_area(10))

"""
Write a function to find the area of a decagon.
assert decagon_area(10)==1309.391
"""
def decagon_area(side):
    return 2*(1+2*0.6234898018587335)*side**2

print(decagon_area