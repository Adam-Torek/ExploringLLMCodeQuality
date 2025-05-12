"""
Write a function to find the median length of a trapezium.
assert median_trapezium(15,25,35)==20
"""

def median_trapezium(a,b,c):
    return (a+b+c)/2

print(median_trapezium(15,25,35))

"""
Write a function to find the area of a trapezium.
assert area_trapezium(15,25,35)==125
"""

def area_trapezium(a,b,c):
    return (a+b)*c/2

print(area_trapezium(15,25,35))

"""
Write a function to find the area of a triangle.
assert area_triangle(15,25,35)==125
"""

def area_triangle(a,b,c):
    return (a*b*c)/2

print(area_triangle(15,25,35))

"""
Write a function to find the area of a circle.
assert area_circle(15)==706.8583470577035
"""

def area_circle(r):
    return 3.14*r*r

print(area_circle(15))

"""
Write a function to find the area of a square.
assert area_square(15)==225
"""

def area_square(a):
    return a*a

print(area_square(15))

"""
Write a function to find the area of a rectangle.
assert area_rectangle(15,25)==375
"""

def area_rectangle(a,b):
    return a*b

print(area_rectangle(15,25))

"""
Write a function to find the area of a parallelogram.
assert area_parallelogram(15,25)==375
"""

def area_parallelogram(a,b):
    return a*b

print(area_parallelogram(15,25))

"""
Write a function to find the area of a rhombus.
assert area_rhombus(15,25)==375
"""

def area_rhombus(a,b):
    return a*b

print(area_rhombus(15,25))

"""
Write a function to find the area of a regular polygon.
assert area_regular_polygon(15,25)==375
"""

def area_regular_polygon(a,b):
    return a*b

print(area_regular_polygon(15,25))

"""
Write a function to find the area of a regular hexagon.
assert area_regular_hexagon(15)==1131.0342142203421
"""

def area_regular_hexagon(a):
    return 3*a*a*3**0.5/2

print(area_regular_hexagon(15))

"""
Write a function to find the area of a regular octagon.
assert area_regular_octagon(15)==1131.0342142203421
"""

def area_regular_octagon(a):
    return 4*a*a*2**0.5/2

print(area_regular_octagon(15))

"""
Write a function to find the area of a regular decagon.
assert area_regular_decagon(15)==1131.0342142203421
"""

def area_regular_decagon(a):
    return 5*a*a*2**0.5/2

print(area_regular_decagon(15))

"""
Write a function to find the area of a regular dodecagon.
assert area_regular_dodecagon(15)==1131.0342142203421
"""

def area_regular_dodecagon(a):
    return 6*a*a*2**0.5/2

print(area_regular_dodecagon(15))

"""