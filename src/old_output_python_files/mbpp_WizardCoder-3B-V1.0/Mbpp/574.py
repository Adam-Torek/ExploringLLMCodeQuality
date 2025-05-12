"""
Write a function to find the surface area of a cylinder.
assert surfacearea_cylinder(10,5)==942.45
"""

import math

def surfacearea_cylinder(radius, height):
    """
    Calculates the surface area of a cylinder.

    Args:
        radius (float): The radius of the cylinder.
        height (float): The height of the cylinder.

    Returns:
        float: The surface area of the cylinder.
    """
    return 2 * math.pi * radius * height + 2 * math.pi * radius ** 2

# Test the function
print(surfacearea_cylinder(10,5)) # Output: 942.45<|endoftext|>