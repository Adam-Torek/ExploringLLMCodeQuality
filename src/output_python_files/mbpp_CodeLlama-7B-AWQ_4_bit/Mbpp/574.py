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
    return 2 * (radius * radius * 3.14159) + (2 * radius * height)


def test_surfacearea_cylinder():
    assert surfacearea_cylinder(10, 5) == 942.45
    assert surfacearea_cylinder(1, 1) == 12.57
    assert surfacearea_cylinder(10, 1) == 121.94
    assert surfacearea_cylinder(1, 10) == 314.159
    assert surfacearea_cylinder(10, 10) == 3141.59
    assert surfacearea_cylinder(100, 100) == 628318.53
    assert surfacearea_cylinder(1000, 1000) == 6283185.3
    assert surfacearea_cylinder(10000, 10000) == 62831852.7
    assert surfacearea_cylinder(100000, 100000) == 628318527.0
    assert surfacearea_cylinder(1000000, 1000000) == 6283185270.0
    assert surfacearea_cylinder(10000000, 10000000) == 62831852700.0
    assert surfacearea_cylinder(100000000, 100000000) == 628318527000.0
    assert surfacearea_cylinder(1000000000, 1000000000) == 6283185270000.0
    assert surfacearea_cylinder(10000000000, 10000000000) == 62831852700000.0
    assert surfacearea_cylinder(100000000000, 100000000000) == 628318527000000.0
    assert surfacearea_cylinder(1000000000000, 1000000000000) == 6283185270000000.0
    assert surfacearea_cylinder(10000000000000, 10000000000000) == 62831852700000000.0
    assert surfacearea_cylinder(100000000000000, 100000000000000) == 628318527000000000.0
    assert surfacearea_cylinder(1000000000000000, 1000000000000000) == 6283185270000000000.0
    assert surfacearea_cylinder(10000000000000000, 10000000000000000) == 628318527000