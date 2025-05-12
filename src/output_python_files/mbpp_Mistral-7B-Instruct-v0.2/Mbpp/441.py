"""
Write a function to find the surface area of a cube of a given size.
assert surfacearea_cube(5)==150
"""
def surfacearea_cube(size):
    """
    This function calculates the surface area of a cube with the given size.
    :param size: The side length of the cube
    :return: The surface area of the cube
    """
    surface_area = 6 * (size ** 2)
    return surface_area

assert surfacearea_cube(5) == 150