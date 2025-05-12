"""
Write a function to find the lateral surface area of a cube given its side length.
assert lateralsurface_cube(5)==100
"""

def lateralsurface_cube(s):
    """
    This function calculates the lateral surface area of a cube.
    The cube has 6 faces, each of which is a square.
    The side length of the cube is given as an input parameter.
    The function returns the lateral surface area of the cube.
    """
    return 6*s**2