"""
Write a function to find the circumference of a circle.
assert math.isclose(circle_circumference(10), 62.830000000000005, rel_tol=0.001)
"""

import math

def circle_circumference(radius):
    return 2 * math.pi * radius

print(circle_circumference(10))

# Test the function
assert math.isclose(circle_circumference(10), 62.83000000000005, rel_tol=0.001)

# Test the function with another value
assert math.isclose(circle_circumference(5), 31.4159, rel_tol=0.001)

# Test the function with another value
assert math.isclose(circle_circumference(15), 94.2477, rel_tol=0.001)

# Test the function with another value
assert math.isclose(circle_circumference(20), 125.6637, rel_tol=0.001)

# Test the function with another value
assert math.isclose(circle_circumference(1), 6.283, rel_tol=0.001)

# Test the function with another value
assert math.isclose(circle_circumference(0), 0, rel_tol=0.001)

# Test the function with another value
assert math.isclose(circle_circumference(100), 628.300, rel_tol=0.001)

# Test the function with another value
assert math.isclose(circle_circumference(2.5), 19.634, rel_tol=0.001)

# Test the function with another value
assert math.isclose(circle_circumference(0.5), 3.1415, rel_tol=0.001)

# Test the function with another value
assert math.isclose(circle_circumference(3.14, rel_tol=0.001)

# Test the function with another value
assert math.isclose(circle_circumference(1000), 628.300, rel_tol=0.001)

# Test the function with another value
assert math.isclose(circle_circumference(0.001), 0.0628, rel_tol=0.001)

# Test the function with another value
assert math.isclose(circle_circumference(0.0001), 0.00628, rel_tol=0.001)

# Test the function with another value
assert math.isclose(circle_circumference(0.00001), 0.000628, rel_tol=0.001)

# Test the function with another value
assert math.isclose(circle_circumference(0.000001), 0.0000628, rel_tol=0.001)

# Test the function with another value
assert math.isclose(circle_circumference(0.0000001), 0.00000628, rel_tol=0.001)

# Test the function with another value
assert math.isclose(circle_circumference(0.00000001), 0.000000628, rel_tol=0.001)

# Test the function with another value
assert math.isclose(circle_circumference(0.000000001), 0.000000628, rel_tol=0.001)

# Test the function with another value
assert math.isclose(circle_circumference(0.0000000001), 0.000000628, rel_tol=0.001)

# Test the function with another value
assert math.