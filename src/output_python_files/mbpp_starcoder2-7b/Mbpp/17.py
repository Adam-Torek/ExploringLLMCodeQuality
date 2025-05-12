"""
Write a function that returns the perimeter of a square given its side length as input.
assert square_perimeter(10)==40
"""
def square_perimeter(side):
    return side * 4

"""
Write a function that returns the perimeter of a rectangle given its length and width as input.
assert rectangle_perimeter(10, 20)==60
"""
def rectangle_perimeter(length, width):
    return length * 2 + width * 2

"""
Write a function that returns the perimeter of a triangle given its side length as input.
assert triangle_perimeter(10)==30
"""
def triangle_perimeter(side):
    return side * 3

"""
Write a function that returns the area of a square given its side length as input.
assert square_area(10)==100
"""
def square_area(side):
    return side ** 2

"""
Write a function that returns the area of a rectangle given its length and width as input.
assert rectangle_area(10, 20)==200
"""
def rectangle_area(length, width):
    return length * width

"""
Write a function that returns the area of a triangle given its side length as input.
assert triangle_area(10)==50
"""
def triangle_area(side):
    return (side ** 2) * (math.sqrt(3)) / 4

"""
Write a function that returns the volume of a cube given its side length as input.
assert cube_volume(10)==1000
"""
def cube_volume(side):
    return side ** 3

"""
Write a function that returns the volume of a rectangular prism given its length, width, and height as input.
assert rectangular_prism_volume(10, 20, 30)==6000
"""
def rectangular_prism_volume(length, width, height):
    return length * width * height

"""
Write a function that returns the volume of a cylinder given its radius and height as input.
assert cylinder_volume(10, 20)==6000
"""
def cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height

"""
Write a function that returns the volume of a cone given its radius and height as input.
assert cone_volume(10, 20)==1000
"""
def cone_volume(radius, height):
    return (math.pi * radius ** 2 * height) / 3

"""
Write a function that returns the volume of a sphere given its radius as input.
assert sphere_volume(10)==4188.79
"""
def sphere_volume(radius):
    return (4 / 3) * math.pi * radius ** 3

"""
Write a function that returns the surface area of a cube given its side length as input.
assert cube_surface_area(10)==200
"""
def cube_surface_area(side):
    return 6 * side ** 2

"""
Write a function that returns the surface area of a rectangular prism given its length, width, and height as input.
assert rectangular_prism_surface_area(10, 20, 30)==1200
"""
def rectangular_prism_surface_area(length, width, height):
    return 2 * (length * width + length * height + width * height)

"""
Write a function that returns the surface area of a cylinder given its radius and height as input.
assert cylinder_surface_area(10, 20)==628.3185307179586
"""
def cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

"""
Write a function that returns the surface area of a cone given its radius and height as input.
assert cone_surface_area(10, 20)==235.6194490192345
"""
def cone_surface_area(radius, height):
    return math.pi * radius * (radius + math