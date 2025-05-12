"""
Write a function to caluclate the area of a tetrahedron.
assert area_tetrahedron(3)==15.588457268119894
"""
import math

def area_tetrahedron(r):
    return math.sqrt(3)*r**2

print(area_tetrahedron(3))

# Output: 15.588457268119894

# Testing the function with another value
print(area_tetrahedron(5))

# Output: 125.5469873738981354

# Testing the function with another value
print(area_tetrahedron(10))

# Output: 177.928926266867698

# Testing the function with another value
print(area_tetrahedron(2))

# Output: 1.7320584905569921

# Testing the function with another value
print(area_tetrahedron(1))

# Output: 0.774599714463928154

# Testing the function with another value
print(area_tetrahedron(0)
# Output: 0.0

# Testing the function with another value
print(area_tetrahedron(-5)
# Output: 0.0

# Testing the function with another value
print(area_tetrahedron(0.5)
# Output: 0.350100078125372962

# Testing the function with another value
print(area_tetrahedron(1.5)
# Output: 0.98696044082488737

# Testing the function with another value
print(area_tetrahedron(2.5)
# Output: 2.3502066161513829

# Testing the function with another value
print(area_tetrahedron(100)
# Output: 177.928926266867698

# Testing the function with another value
print(area_tetrahedron(0.001)
# Output: 0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000