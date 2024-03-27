"""
Write a function to find the volume of a cone.
assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)
"""
import math

def volume_cone(radius, height):
    """
    Calculate the volume of a cone with given radius and height
    :param radius: float, the radius of the base of the cone
    :param height: float, the height of the cone
    :return: float, the volume of the cone
    """
    volume = (1.0/3.0) * math.pi * (radius ** 2) * height
    return volume</s>