"""
Write a function that takes in the radius and height of a cylinder and returns the the volume.
assert math.isclose(volume_cylinder(10,5), 1570.7500000000002, rel_tol=0.001)
"""
import math

def volume_cylinder(radius, height):
    """
    Calculates the volume of a cylinder given its radius and height.

    Args:
        radius (float): The radius of the cylinder.
        height (float): The height of the cylinder.

    Returns:
        float: The volume of the cylinder.
    """
    volume = math.pi * (radius ** 2) * height
    return volume