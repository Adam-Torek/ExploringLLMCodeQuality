"""
Write a function to find the lateral surface area of a cone given radius r and the height h.
assert lateralsurface_cone(5,12)==204.20352248333654
"""
import math

def lateralsurface_cone(r, h):
    """
    Function to find the lateral surface area of a cone given radius r and height h
    :param r: radius of the cone
    :param h: height of the cone
    :return: lateral surface area of the cone
    """
    lateral_surface_area = math.pi * r * math.sqrt(r**2 + h**2)
    return lateral_surface_area

assert lateralsurface_cone(5,12) == 204.20352248333654</s>