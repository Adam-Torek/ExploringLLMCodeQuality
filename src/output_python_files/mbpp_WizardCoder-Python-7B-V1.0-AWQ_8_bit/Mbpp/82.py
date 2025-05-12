"""
Write a function to find the volume of a sphere.
assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)
"""
import math

def volume_sphere(radius):
    return 4/3 * math.pi * radius ** 3

print(volume_sphere(10))

# Test the function with the given value
assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)

# Test the function with another value
assert math.isclose(volume_sphere(5), 523.6, rel_tol=0.001)

# Test the function with another value
assert math.isclose(volume_sphere(1), 4.188790204786391, rel_tol=0.001)

# Test the function with another value
assert math.isclose(volume_sphere(0), 0, rel_tol=0.001)

# Test the function with another value
assert math.isclose(volume_sphere(100), 15330.17, rel_tol=0.001)

# Test the function with another value
assert math.isclose(volume_sphere(1000), 1.7139771828690968e+11, rel_tol=0.001)

# Test the function with another value
assert math.isclose(volume_sphere(0.5), 1.557, rel_tol=0.001)

# Test the function with another value
assert math.isclose(volume_sphere(2.5), 111.13, rel_tol=0.001)

# Test the function with another value
assert math.isclose(volume_sphere(7.6), 1.571, rel_tol=0.001)

# Test the function with another value
assert math.isclose(volume_sphere(10000), 1.7139771828690968e+11, rel_tol=0.001)

# Test the function with another value
assert math.isclose(volume_sphere(0.001), 0.0000704, rel_tol=0.001)

# Test the function with another value
assert math.isclose(volume_sphere(0.000001), 7.04e-06, rel_tol=0.001)

# Test the function with another value
assert math.isclose(volume_sphere(0.0000001), 7.04e-09, rel_tol=0.001)

# Test the function with another value
assert math.isclose(volume_sphere(0.00000001), 7.04e-12, rel_tol=0.001)

# Test the function with another value
assert math.isclose(volume_sphere(0.0000000001), 7.04e-15, rel_tol=0.001)

# Test the function with another value
assert math.isclose(volume_sphere(0.00000000000001), 7.04e-18, rel_tol=0.001)

# Test the function with another value
assert math.isclose(volume_sphere(0.00000000000000001), 7.04e-21, rel_tol=0.001)

# Test the function with another value
assert math.isclose(volume_sphere(0.000000000000000001), 7.04e-24, rel_tol=0.001)

# Test the function with another value
assert