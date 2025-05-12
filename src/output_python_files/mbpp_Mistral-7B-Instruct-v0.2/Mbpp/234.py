"""
Write a function to find the volume of a cube given its side length.
assert volume_cube(3)==27
"""
def volume_cube(side_length):
    """
    Function to find the volume of a cube given its side length
    :param side_length: int or float
    :return: int or float
    """
    volume = side_length ** 3
    return volume

assert volume_cube(3) == 27