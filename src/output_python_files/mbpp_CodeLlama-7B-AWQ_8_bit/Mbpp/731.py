"""
Write a function to find the lateral surface area of a cone given radius r and the height h.
assert lateralsurface_cone(5,12)==204.20352248333654
"""


def lateralsurface_cone(r, h):
    """
    :param r: radius of the cone
    :param h: height of the cone
    :return: lateral surface area of the cone
    """
    return 2 * r * h + 2 * math.pi * r * r


if __name__ == '__main__':
    print(lateralsurface_cone(5, 12))
    print(lateralsurface_cone(10, 15))
    print(lateralsurface_cone(1, 1))
    print(lateralsurface_cone(10, 1))
    print(lateralsurface_cone(1, 10))
    print(lateralsurface_cone(10, 10))
    print(lateralsurface_cone(10, 100))
    print(lateralsurface_cone(100, 10))
    print(lateralsurface_cone(100, 100))
    print(lateralsurface_cone(1000, 100))
    print(lateralsurface_cone(100, 1000))
    print(lateralsurface_cone(1000, 1000))
    print(lateralsurface_cone(10000, 1000))
    print(lateralsurface_cone(1000, 10000))
    print(lateralsurface_cone(10000, 10000))
    print(lateralsurface_cone(100000, 10000))
    print(lateralsurface_cone(10000, 100000))
    print(lateralsurface_cone(100000, 100000))
    print(lateralsurface_cone(1000000, 100000))
    print(lateralsurface_cone(100000, 1000000))
    print(lateralsurface_cone(1000000, 1000000))
    print(lateralsurface_cone(10000000, 1000000))
    print(lateralsurface_cone(1000000, 10000000))
    print(lateralsurface_cone(10000000, 10000000))
    print(lateralsurface_cone(100000000, 10000000))
    print(lateralsurface_cone(10000000, 100000000))
    print(lateralsurface_cone(100000000, 100000000))
    print(lateralsurface_cone(1000000000, 100000000))
    print(lateralsurface_cone(100000000, 1000000000))
    print(lateralsurface_cone(1000000000, 1000000000))
    print(lateralsurface_cone(10000000000, 1000000000))
    print(lateralsurface_cone(1000000000, 10000000000))
    print(laterals