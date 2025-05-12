"""
Write a function to find the lateral surface area of a cube given its side length.
assert lateralsurface_cube(5)==100
"""
def lateralsurface_cube(side_length):
    """
    This function calculates the lateral surface area of a cube given its side length
    :param side_length: the length of a side of the cube
    :return: the lateral surface area of the cube
    """
    lateral_surface_area = 6 * (side_length ** 2)
    return lateral_surface_area

assert lateralsurface_cube(5) == 100