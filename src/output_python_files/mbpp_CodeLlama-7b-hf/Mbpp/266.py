"""
Write a function to find the lateral surface area of a cube given its side length.
assert lateralsurface_cube(5)==100
"""


def lateralsurface_cube(side):
    """
    :param side: side length of cube
    :return: lateral surface area of cube
    """
    return 6 * side ** 2


if __name__ == '__main__':
    print(lateralsurface_cube(5))