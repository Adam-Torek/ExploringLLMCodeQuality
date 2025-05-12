"""
Write a function to find the surface area of a cylinder.
assert surfacearea_cylinder(10,5)==942.45
"""


def surfacearea_cylinder(radius, height):
    """
    :param radius: radius of the cylinder
    :param height: height of the cylinder
    :return: surface area of the cylinder
    """
    return 2 * (radius * radius * 3.14) + (2 * radius * height)


if __name__ == '__main__':
    print(surfacearea_cylinder(10, 5))
    print(surfacearea_cylinder(5, 10))
    print(surfacearea_cylinder(10, 10))
    print(surfacearea_cylinder(1, 1))
    print(surfacearea_cylinder(1, 10))
    print(surfacearea_cylinder(10, 1))
    print(surfacearea_cylinder(10, 100))
    print(surfacearea_cylinder(100, 10))
    print(surfacearea_cylinder(100, 100))
    print(surfacearea_cylinder(1000, 1000))
    print(surfacearea_cylinder(10000, 10000))
    print(surfacearea_cylinder(100000, 100000))
    print(surfacearea_cylinder(1000000, 1000000))
    print(surfacearea_cylinder(10000000, 10000000))
    print(surfacearea_cylinder(100000000, 100000000))
    print(surfacearea_cylinder(1000000000, 1000000000))
    print(surfacearea_cylinder(10000000000, 10000000000))
    print(surfacearea_cylinder(100000000000, 100000000000))
    print(surfacearea_cylinder(1000000000000, 1000000000000))
    print(surfacearea_cylinder(10000000000000, 10000000000000))
    print(surfacearea_cylinder(100000000000000, 100000000000000))
    print(surfacearea_cylinder(1000000000000000, 1000000000000000))
    print(surfacearea_cylinder(10000000000000000, 10000000000000000))
    print(surfacearea_cylinder(100000000000000000, 100000000000000000))
    print(surfacearea_cylinder(1000000000000000000, 1000000000000000000))
    print(surfacearea_cylinder(10000000000000000000, 10000000000000000000))
    print(surfacearea_cylinder(10000000