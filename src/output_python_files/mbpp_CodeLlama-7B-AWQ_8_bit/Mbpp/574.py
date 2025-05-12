"""
Write a function to find the surface area of a cylinder.
assert surfacearea_cylinder(10,5)==942.45
"""


def surfacearea_cylinder(radius, height):
    """
    radius: float or int
    height: float or int
    returns: float
    """
    return 2 * radius * height + 2 * math.pi * radius * radius


def surfacearea_cylinder_test_case(radius, height):
    """
    Tests surfacearea_cylinder for a given radius and height.
    """
    print("radius:", radius, " height:", height, " area:", surfacearea_cylinder(radius, height))


def surfacearea_cylinder_test():
    """
    Tests surfacearea_cylinder for:
    radius: 10, height: 5
    radius: 1, height: 1
    radius: 2, height: 3
    radius: 4, height: 5
    radius: 8, height: 9
    radius: 10, height: 10
    radius: 100, height: 100
    radius: 1000, height: 1000
    radius: 10000, height: 10000
    radius: 100000, height: 100000
    radius: 1000000, height: 1000000
    radius: 10000000, height: 10000000
    radius: 100000000, height: 100000000
    radius: 1000000000, height: 1000000000
    radius: 10000000000, height: 10000000000
    radius: 100000000000, height: 100000000000
    radius: 1000000000000, height: 1000000000000
    radius: 10000000000000, height: 10000000000000
    radius: 100000000000000, height: 100000000000000
    radius: 1000000000000000, height: 1000000000000000
    radius: 10000000000000000, height: 10000000000000000
    radius: 100000000000000000, height: 100000000000000000
    radius: 1000000000000000000, height: 1000000000000000000
    radius: 10000000000000000000, height: 10000000000000000000
    radius: 100000000000000000000, height: 100000000000000000000
    radius: 1000000000000000000000, height: 1000000000000000000000
    radius: 10000000000000000000000, height: 10000000000000000000000
    radius: 100000000000000