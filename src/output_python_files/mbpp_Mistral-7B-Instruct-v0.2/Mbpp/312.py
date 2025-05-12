"""
Write a function to find the volume of a cone.
assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)
"""
import math

def volume_cone(radius, height):
    """
    Calculate the volume of a cone with given radius and height.

    Args:
        radius (float): The radius of the base of the cone.
        height (float): The height of the cone.

    Returns:
        float: The volume of the cone.
    """
    volume = (1.0/3.0) * math.pi * (radius ** 2) * height
    return volume