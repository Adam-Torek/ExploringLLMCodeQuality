"""
Write a function that takes in the radius and height of a cylinder and returns the the volume.
assert math.isclose(volume_cylinder(10,5), 1570.7500000000002, rel_tol=0.001)
"""
import math

def volume_cylinder(radius, height):
    return math.pi * radius ** 2 * height

print(volume_cylinder(10,5))

# Test the function with the given test case
assert math.isclose(volume_cylinder(10,5), 1570.750000000002, rel_tol=0.001)

# Test the function with additional test cases
assert math.isclose(volume_cylinder(2, 10), 1256.636, rel_tol=0.001)
assert math.isclose(volume_cylinder(5, 7), 1013.672, rel_tol=0.001)
assert math.isclose(volume_cylinder(1, 3), 12.5664, rel_tol=0.001)
assert math.isclose(volume_cylinder(0, 10), 0, rel_tol=0.001)
assert math.isclose(volume_cylinder(10, 0), 0, rel_tol=0.001)
assert math.isclose(volume_cylinder(0, 0), 0, rel_tol=0.001)

# Test the function with edge cases
assert math.isclose(volume_cylinder(0, 1), 0, rel_tol=0.001)
assert math.isclose(volume_cylinder(1, 0), 0, rel_tol=0.001)
assert math.isclose(volume_cylinder(-1, 1), 0, rel_tol=0.001)
assert math.isclose(volume_cylinder(1, -1), 0, rel_tol=0.001)
assert math.isclose(volume_cylinder(-1, -1), 0, rel_tol=0.001)
assert math.isclose(volume_cylinder(1, 1), 3.1416, rel_tol=0.001)
assert math.isclose(volume_cylinder(-1, 1), 0, rel_tol=0.001)
assert math.isclose(volume_cylinder(1, -1), 0, rel_tol=0.001)
assert math.isclose(volume_cylinder(-1, -1), 0, rel_tol=0.001)

# Test the function with other edge cases
assert math.isclose(volume_cylinder(100, 100), 31415.9, rel_tol=0.001)
assert math.isclose(volume_cylinder(1000, 1000), 314159, rel_tol=0.001)
assert math.isclose(volume_cylinder(10000, 10000), 3141590, rel_tol=0.001)
assert math.isclose(volume_cylinder(100000, 100000), 31415900, rel_tol=0.001)
assert math.isclose(volume_cylinder(1000000, 1000000), 314159000, rel_tol=0.001)
assert math.isclose(volume_cylinder(10000000, 10000000), 3141590000, rel_tol=0.0