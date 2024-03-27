"""
Write a function to find the volume of a cube given its side length.
assert volume_cube(3)==27
"""
def volume_cube(side_length):
    """
    This function calculates the volume of a cube given its side length
    :param side_length: the length of a side of the cube
    :return: the volume of the cube
    """
    volume = side_length ** 3
    return volume

# Test the function
assert volume_cube(3) == 27</s>