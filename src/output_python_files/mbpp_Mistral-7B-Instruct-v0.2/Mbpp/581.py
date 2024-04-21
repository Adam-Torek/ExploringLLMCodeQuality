"""
Write a python function to find the surface area of a square pyramid with a given base edge and height.
assert surface_Area(3,4) == 33
"""
def surface_Area(base_edge, height):
    """
    This function calculates the surface area of a square pyramid given its base edge and height.

    Parameters:
    base_edge (int): The length of one side of the square base of the pyramid.
    height (int): The height of the pyramid.

    Returns:
    int: The surface area of the pyramid.
    """
    # Calculate the area of the base square
    base_area = base_edge ** 2

    # Calculate the area of the four triangular faces
    half_base = base_edge / 2
    height_of_triangle = math.sqrt((base_edge / 2) ** 2 + (height ** 2))
    triangle_area = 4 * (0.5 * base_edge * height_of_triangle)

    # Calculate the total surface area
    total_surface_area = base_area + 4 * triangle_area

    # Return the result
    return int(total_surface_area)

# Test the function
import math
assert surface_Area(3, 4) == 33</s>