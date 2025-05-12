"""
Write a python function to find the surface area of a square pyramid with a given base edge and height.
assert surface_Area(3,4) == 33
"""

def surface_Area(base_edge, height):
    """
    This function calculates the surface area of a square pyramid.
    :param base_edge: the length of one edge of the square base
    :param height: the height of the pyramid
    :return: the surface area of the pyramid
    """
    # calculate the area of the square base
    base_area = base_edge ** 2
    # calculate the lateral surface area of the pyramid
    lateral_area = 4 * base_edge * height
    # calculate the top and bottom areas of the pyramid
    top_area = base_area
    bottom_area = 0
    # add all the areas together to get the total surface area
    total_area = base_area + lateral_area + top_area + bottom_area
    return total_area

# test the function
assert surface_Area(3,4) == 33