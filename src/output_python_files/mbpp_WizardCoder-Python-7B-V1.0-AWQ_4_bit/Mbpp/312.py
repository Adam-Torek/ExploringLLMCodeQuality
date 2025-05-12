"""
Write a function to find the volume of a cone.
assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)
"""

import math

def volume_cone(radius, height):
    return (1/3) * math.pi * radius**2 * height

print(volume_cone(5,12))

# Test the function with the given test case
assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)

# Test the function with additional test cases
assert math.isclose(volume_cone(10, 20), 1256.6379999999999998, rel_tol=0.001)
assert math.isclose(volume_cone(1, 10), 12.56637061410056738, rel_tol=0.001)
assert math.isclose(volume_cone(0, 10), 0, rel_tol=0.001)
assert math.isclose(volume_cone(10, 0), 0, rel_tol=0.001)
assert math.isclose(volume_cone(0, 0), 0, rel_tol=0.001)
assert math.isclose(volume_cone(1, 1), math.pi, rel_tol=0.001)
assert math.isclose(volume_cone(1, 2), 2*math.pi, rel_tol=0.001)
assert math.isclose(volume_cone(2, 1), 12.56637061410056738, rel_tol=0.001)
assert math.isclose(volume_cone(10, 10), 157.0796326794896652, rel_tol=0.001)
assert math.isclose(volume_cone(100, 100), 31415.926535897927, rel_tol=0.001)
assert math.isclose(volume_cone(1000, 1000), 314159.26535897927, rel_tol=0.001)

# Test the function with edge cases
assert math.isclose(volume_cone(0, 100), 0, rel_tol=0.001)
assert math.isclose(volume_cone(100, 0), 0, rel_tol=0.001)
assert math.isclose(volume_cone(0, 0), 0, rel_tol=0.001)
assert math.isclose(volume_cone(1, 1), math.pi, rel_tol=0.001)
assert math.isclose(volume_cone(1, 2), 2*math.pi, rel_tol=0.001)
assert math.isclose(volume_cone(2, 1), 12.56637061410056738, rel_tol=0.001)
assert math.isclose(volume_cone(100, 100), 31415.926535897927, rel_tol=0.001)
assert math.isclose(volume_cone(1000, 1000), 314159.26535897927, rel_tol=0.001)

# Test the function with negative values
assert math.isclose(volume_cone(-5, 12), 0, rel_tol=0.001)
assert math.isclose(volume_cone(5, -12), 0