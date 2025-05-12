"""
Write a function to find the volume of a sphere.
assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)
"""

import math

def volume_sphere(radius):
    return 4/3 * math.pi * radius**3

# Test the function
print(volume_sphere(10))

# Test the function with a tolerance of 0.001
assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)

# Test the function with a tolerance of 0.001
assert math.isclose(volume_sphere(5), 523.6, rel_tol=0.001)

# Test the function with a tolerance of 0.001
assert math.isclose(volume_sphere(1), 4.188790204786391, rel_tol=0.001)

# Test the function with a tolerance of 0.001
assert math.isclose(volume_sphere(0), 0, rel_tol=0.001)

# Test the function with a tolerance of 0.001
assert math.isclose(volume_sphere(2.5), 158.54, rel_tol=0.001)

# Test the function with a tolerance of 0.001
assert math.isclose(volume_sphere(7.6, rel_tol=0.001)