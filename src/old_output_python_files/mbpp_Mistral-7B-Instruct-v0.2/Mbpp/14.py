"""
Write a python function to find the volume of a triangular prism.
assert find_Volume(10,8,6) == 240
"""
def find_Volume(length, width, height):
    """
    This function calculates the volume of a triangular prism
    :param length: The length of the base of the triangular prism
    :param width: The width of the base of the triangular prism
    :param height: The height of the triangular prism
    :return: The volume of the triangular prism
    """
    volume_triangle = 0.5 * length * width
    volume_prism = length * width * height
    return volume_triangle + volume_prism

assert find_Volume(10,8,6) == 240