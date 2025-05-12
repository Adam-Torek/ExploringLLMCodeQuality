"""
Write a function that takes in the radius and height of a cylinder and returns the the volume.
assert math.isclose(volume_cylinder(10,5), 1570.7500000000002, rel_tol=0.001)
"""

import math

def volume_cylinder(radius, height):
    return math.pi * radius ** 2 * height


def test_volume_cylinder():
    assert math.isclose(volume_cylinder(10,5), 1570.7500000000002, rel_tol=0.001)
    assert math.isclose(volume_cylinder(10,10), 3141.592653589793, rel_tol=0.001)
    assert math.isclose(volume_cylinder(10,15), 7853.981633974483, rel_tol=0.001)
    assert math.isclose(volume_cylinder(10,20), 15707.500000000002, rel_tol=0.001)
    assert math.isclose(volume_cylinder(10,25), 25707.500000000002, rel_tol=0.001)
    assert math.isclose(volume_cylinder(10,30), 35707.500000000002, rel_tol=0.001)
    assert math.isclose(volume_cylinder(10,35), 45707.500000000002, rel_tol=0.001)
    assert math.isclose(volume_cylinder(10,40), 55707.500000000002, rel_tol=0.001)
    assert math.isclose(volume_cylinder(10,45), 65707.500000000002, rel_tol=0.001)
    assert math.isclose(volume_cylinder(10,50), 75707.500000000002, rel_tol=0.001)
    assert math.isclose(volume_cylinder(10,55), 85707.500000000002, rel_tol=0.001)
    assert math.isclose(volume_cylinder(10,60), 95707.500000000002, rel_tol=0.001)
    assert math.isclose(volume_cylinder(10,65), 105707.500000000002, rel_tol=0.001)
    assert math.isclose(volume_cylinder(10,70), 115707.500000000002, rel_tol=0.001)
    assert math.isclose(volume_cylinder(10,75), 125707.500000000002, rel_tol=0.001)
    assert math.isclose(volume_cylinder(10,80), 135707.500000000002, rel_tol=0.001)
    assert math.isclose(volume_cylinder(10,85), 145707.500000000002, rel_tol=0.001)
    assert math.isclose(