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
assert math.isclose(volume_cylinder(2, 3), 125.13, rel_tol=0.001)
assert math.isclose(volume_cylinder(5, 7), 1013.97, rel_tol=0.001)
assert math.isclose(volume_cylinder(1, 10), 314.159, rel_tol=0.001)

# Test the function with edge cases
assert math.isclose(volume_cylinder(0, 10), 0, rel_tol=0.001)
assert math.isclose(volume_cylinder(10, 0), 0, rel_tol=0.001)
assert math.isclose(volume_cylinder(0, 0), 0, rel_tol=0.001)
assert math.isclose(volume_cylinder(10, -5), 0, rel_tol=0.001)
assert math.isclose(volume_cylinder(-5, 10), 0, rel_tol=0.001)
assert math.isclose(volume_cylinder(-5, -5), 0, rel_tol=0.001)
assert math.isclose(volume_cylinder(5, -5), 0, rel_tol=0.001)

# Test the function with invalid input
try:
    volume_cylinder("a", 5)
except TypeError:
    print("The function should only accept numbers as input")

try:
    volume_cylinder(10, "b")
except TypeError:
    print("The function should only accept numbers as input")

try:
    volume_cylinder(10, [5])
except TypeError:
    print("The function should only accept numbers as input")

try:
    volume_cylinder(10, (5, 6))
except TypeError:
    print("The function should only accept numbers as input")

try:
    volume_cylinder(10, None)
except TypeError:
    print("The function should only accept numbers as input")

try:
    volume_cylinder(10, 5, 6)
except TypeError:
    print("The function should only accept two arguments")

try:
    volume_cylinder(10)
except TypeError:
    print("The function should only accept two arguments")

try:
    volume_cylinder(10, 5, 6)
except TypeError:
    print("The function should only accept two arguments")

try:
    volume_cylinder(10, -5)
except ValueError:
    print("The radius and height should be positive numbers")

try:
    volume_cylinder(-5, 10)
except ValueError:
    print("The radius and height should be positive numbers")

try:
    volume_cylinder(-5, -5)
except ValueError:
    print("The radius and height should be positive numbers")

try:
    volume_cylinder(0, 10)
except ValueError:
    print("The radius and height should be positive numbers")

try:
    volume_cylinder(10, 0)
except ValueError:
    print("The radius and height should be positive numbers")

try:
    volume_cylinder(0, 0)
except ValueError:
    print("The radius and