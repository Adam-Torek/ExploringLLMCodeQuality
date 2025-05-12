"""
Write a function that returns the perimeter of a square given its side length as input.
assert square_perimeter(10)==40
"""

def square_perimeter(side):
    return side * 4

print(square_perimeter(10))

"""
Write a function that returns the perimeter of a rectangle given its length and width as input.
assert rectangle_perimeter(10, 20)==60
"""

def rectangle_perimeter(length, width):
    return length * 2 + width * 2

print(rectangle_perimeter(10, 20))

"""
Write a function that returns the perimeter of a triangle given its length and width as input.
assert triangle_perimeter(10, 20)==30
"""

def triangle_perimeter(length, width):
    return length + length + width

print(triangle_perimeter(10, 20))

"""
Write a function that returns the perimeter of a circle given its radius as input.
assert circle_perimeter(10)==62.83185307179586
"""

def circle_perimeter(radius):
    return 2 * 3.14 * radius

print(circle_perimeter(10))

"""
Write a function that returns the perimeter of a regular polygon given its number of sides and length of each side as input.
assert regular_polygon_perimeter(10, 20)==200
"""

def regular_polygon_perimeter(sides, length):
    return sides * length

print(regular_polygon_perimeter(10, 20))

"""
Write a function that returns the perimeter of a regular polygon given its number of sides and its apothem as input.
assert regular_polygon_perimeter(10, 20)==200
"""

def regular_polygon_perimeter(sides, apothem):
    return sides * apothem * 2

print(regular_polygon_perimeter(10, 20))

"""
Write a function that returns the perimeter of a regular polygon given its number of sides and its side length as input.
assert regular_polygon_perimeter(10, 20)==200
"""

def regular_polygon_perimeter(sides, side_length):
    return sides * side_length

print(regular_polygon_perimeter(10, 20))

"""
Write a function that returns the perimeter of a regular polygon given its number of sides and its circumradius as input.
assert regular_polygon_perimeter(10, 20)==200
"""

def regular_polygon_perimeter(sides, circumradius):
    return sides * circumradius * 2

print(regular_polygon_perimeter(10, 20))

"""
Write a function that returns the perimeter of a regular polygon given its number of sides and its inradius as input.
assert regular_polygon_perimeter(10, 20)==200
"""

def regular_polygon_perimeter(sides, inradius):
    return sides * inradius * 2

print(regular_polygon_perimeter(10, 20))

"""
Write a function that returns the perimeter of a regular polygon given its number of sides and its area as input.
assert regular_polygon_perimeter(10, 20)==200
"""

def regular_polygon_perimeter(sides, area):
    return sides * (area / sides) * 2

print(regular_polygon_perimeter(10, 20))

"""
Write a function that returns the perimeter of a regular polygon given its number of sides and its side length as input.
assert regular_polygon_perimeter(10, 20)==200
"""

def regular_polygon_perimeter(sides, side_length):
    return sides * side_length

print(regular_polygon_perimeter(10, 20))

"""
Write a function that returns the perimeter of a regular polygon given its number of sides and its apothem as input.
assert regular_polygon_perimeter(10, 20)==200
"""

def regular_polygon_perimeter(sides, apothem):
    return sides * apothem * 2

print(regular_polygon_perimeter(