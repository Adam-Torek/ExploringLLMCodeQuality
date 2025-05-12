"""
Write a function to find the lateral surface area of a cone given radius r and the height h.
assert lateralsurface_cone(5,12)==204.20352248333654
"""
import math

def lateralsurface_cone(r, h):
    """
    Calculate the lateral surface area of a cone given its radius and height.
    :param r: The radius of the base of the cone.
    :param h: The height of the cone.
    :return: The lateral surface area of the cone.
    """
    lateral_surface_area = math.pi * r * math.sqrt(r**2 + h**2)
    return lateral_surface_area

assert lateralsurface_cone(5, 12) == 204.20352248333654