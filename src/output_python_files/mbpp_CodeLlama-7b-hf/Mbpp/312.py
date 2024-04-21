"""
Write a function to find the volume of a cone.
assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)
"""

import math

def volume_cone(radius, height):
    """
    Calculate the volume of a cone.
    """
    return (1/3) * math.pi * (radius ** 2) * height


def test_volume_cone():
    """
    Test the volume_cone function.
    """
    assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)


if __name__ == '__main__':
    test_volume_cone()


"""
Write a function to find the volume of a sphere.
assert math.isclose(volume_sphere(5), 113.0973355292323, rel_tol=0.001)
"""

import math

def volume_sphere(radius):
    """
    Calculate the volume of a sphere.
    """
    return (4/3) * math.pi * (radius ** 3)


def test_volume_sphere():
    """
    Test the volume_sphere function.
    """
    assert math.isclose(volume_sphere(5), 113.0973355292323, rel_tol=0.001)


if __name__ == '__main__':
    test_volume_sphere()


"""
Write a function to find the volume of a cylinder.
assert math.isclose(volume_cylinder(5,12), 157.07963267948966, rel_tol=0.001)
"""

import math

def volume_cylinder(radius, height):
    """
    Calculate the volume of a cylinder.
    """
    return math.pi * (radius ** 2) * height


def test_volume_cylinder():
    """
    Test the volume_cylinder function.
    """
    assert math.isclose(volume_cylinder(5,12), 157.07963267948966, rel_tol=0.001)


if __name__ == '__main__':
    test_volume_cylinder()


"""
Write a function to find the volume of a cuboid.
assert math.isclose(volume_cuboid(5,12,10), 600.0, rel_tol=0.001)
"""

import math

def volume_cuboid(length, width, height):
    """
    Calculate the volume of a cuboid.
    """
    return length * width * height


def test_volume_cuboid():
    """
    Test the volume_cuboid function.
    """
    assert math.isclose(volume_cuboid(5,12,10), 600.0, rel_tol=0.001)


if __name__ == '__main__':
    test_volume_cuboid()


"""
Write a function to find the volume of a rectangular prism.
assert math.isclose(volume_rectangular_prism(5,12,10), 600.0, rel_tol=0.001)
"""

import math

def volume_rectangular_prism(length, width, height):
    """
    Calculate the volume of a rectangular prism.
    """
    return length * width * height


def test_volume_rectangular_prism():
    """
    Test the volume_rectangular_prism function.
    """
    assert math.isclose(volume_rectangular_prism(5,12,10), 600.0, rel_tol=0.001)


if __name__