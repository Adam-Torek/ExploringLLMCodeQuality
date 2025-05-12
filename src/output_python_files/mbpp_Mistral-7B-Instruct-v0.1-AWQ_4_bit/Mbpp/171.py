"""
Write a function to find the perimeter of a regular pentagon from the length of its sides.
assert perimeter_pentagon(5) == 25
"""

from math import sin, cos, pi

def perimeter_pentagon(sides):
    """
    Calculate the perimeter of a regular pentagon.
    """
    angle = 2*pi/sides
    side = s
    perimeter = 0
    for i in range(sides):
        perimeter += side
        side *= cos(angle) - sin(angle)
    return perimeter


if __name__ == '__main__':
    assert perimeter_pentagon(5) == 25