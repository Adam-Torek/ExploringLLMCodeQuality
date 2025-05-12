"""
Write a python function to find the volume of a triangular prism.
assert find_Volume(10,8,6) == 240
"""

def find_Volume(l, w, h):
    """
    :param l: length of the base of the triangle
    :param w: width of the base of the triangle
    :param h: height of the prism
    :return: volume of the triangular prism
    """
    volume = l * w * h
    return volume

#assert find_Volume(10,8,6) == 240