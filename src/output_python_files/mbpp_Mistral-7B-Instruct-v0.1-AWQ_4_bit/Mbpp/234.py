"""
Write a function to find the volume of a cube given its side length.
assert volume_cube(3)==27
"""

def volume_cube(side_length):
    """
    This function calculates the volume of a cube given its side length.
    :param side_length: int or float, the side length of the cube
    :return: int or float, the volume of the cube
    """
    volume = side_length ** 3
    return volume

# test the function
assert volume_cube(3) == 27