"""
Write a function to find the lateral surface area of a cylinder.
assert math.isclose(lateralsuface_cylinder(10,5), 314.15000000000003, rel_tol=0.001)
"""
import math

def lateral_surface_area_cylinder(radius, height):
    """
    Calculates the lateral surface area of a cylinder.

    :param radius: The radius of the base of the cylinder.
    :param height: The height of the cylinder.
    :return: The lateral surface area of the cylinder.
    """
    lateral_surface_area = 2 * math.pi * radius * height
    return lateral_surface_area

if __name__ == "__main__":
    assert math.isclose(lateralsuface_cylinder(10, 5), 314.15000000000003, rel_tol=0.001)
    print("Test passed!")