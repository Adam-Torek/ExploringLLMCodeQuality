"""
Write a function to find the lateral surface area of a cylinder.
assert math.isclose(lateralsuface_cylinder(10,5), 314.15000000000003, rel_tol=0.001)
"""

import math

def lateralsuface_cylinder(radius, height):
    """
    Calculate the lateral surface area of a cylinder.

    Args:
        radius (float): The radius of the cylinder.
        height (float): The height of the cylinder.

    Returns:
        float: The lateral surface area of the cylinder.
    """
    return 2 * math.pi * radius * height

# Test the function
assert math.isclose(lateralsuface_cylinder(10,5), 314.15000000000003, rel_tol=0.001)<|endoftext|>