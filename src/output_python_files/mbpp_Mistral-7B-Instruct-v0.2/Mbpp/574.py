"""
Write a function to find the surface area of a cylinder.
assert surfacearea_cylinder(10,5)==942.45
"""
import math

def surfacearea_cylinder(radius, height):
    """
    Calculate the surface area of a cylinder
    :param radius: float, the radius of the base of the cylinder
    :param height: float, the height of the cylinder
    :return: float, the surface area of the cylinder
    """
    surface_area = 2 * math.pi * radius ** 2 + 2 * math.pi * radius * height
    return surface_area

assert surfacearea_cylinder(10,5) == 942.45</s>