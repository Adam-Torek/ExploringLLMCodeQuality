"""
Write a python function to find the volume of a triangular prism.
assert find_Volume(10,8,6) == 240
"""
def find_Volume(length, width, height):
    """
    This function calculates the volume of a triangular prism.

    Parameters:
    length (float): The length of the base of the triangular prism.
    width (float): The width of the base of the triangular prism.
    height (float): The height of the triangular prism.

    Returns:
    float: The volume of the triangular prism.
    """
    base_area = length * width / 2
    volume = base_area * height
    return volume

assert find_Volume(10, 8, 6) == 240