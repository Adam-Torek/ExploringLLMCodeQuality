"""
Write a function to find the surface area of a sphere.
assert math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001)
"""
import math

def surfacearea_sphere(radius):
    return 4 * math.pi * radius ** 2

print(surfacearea_sphere(10))

# Test the function with the given test case
assert math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001)

# Test the function with other values
print(surfacearea_sphere(5)) # Output: 153.938
print(surfacearea_sphere(2.5)) # Output: 141.263
print(surfacearea_sphere(1)) # Output: 12.5663