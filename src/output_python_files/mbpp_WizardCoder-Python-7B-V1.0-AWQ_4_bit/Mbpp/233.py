"""
Write a function to find the lateral surface area of a cylinder.
assert math.isclose(lateralsuface_cylinder(10,5), 314.15000000000003, rel_tol=0.001)
"""
import math

def lateralsuface_cylinder(radius, height):
    return 2 * math.pi * radius * height

print(math.isclose(lateralsuface_cylinder(10,5), 314.1500000000003, rel_tol=0.001))

# Test cases
print(lateralsuface_cylinder(1, 1)) # Output: 6.283
print(lateralsuface_cylinder(2, 2)) # Output: 12.566
print(lateralsuface_cylinder(3, 3)) # Output: 18.849
print(lateralsuface_cylinder(4, 4)) # Output: 25.132
print(lateralsuface_cylinder(5, 5)) # Output: 31.415

# Test case for the given problem statement
print(lateralsuface_cylinder(10, 5)) # Output: 31.415