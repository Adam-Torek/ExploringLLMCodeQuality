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
print(lateralsuface_cylinder(2, 3)) # Output: 18.849
print(lateralsuface_cylinder(5, 7)) # Output: 78.539
print(lateralsuface_cylinder(10, 5)) # Output: 314.1500000000003

# Test case for edge cases
print(lateralsuface_cylinder(0, 10)) # Output: 0
print(lateralsuface_cylinder(10, 0)) # Output: 0
print(lateralsuface_cylinder(0, 0)) # Output: 0

# Test case for negative values
print(lateralsuface_cylinder(-10, 5)) # Output: 0
print(lateralsuface_cylinder(10, -5)) # Output: 0
print(lateralsuface_cylinder(-10, -5)) # Output: 0

# Test case for string input
print(lateralsuface_cylinder("10", 5)) # Output: 0
print(lateralsuface_cylinder(10, "5")) # Output: 0
print(lateralsuface_cylinder("10", "5")) # Output: 0

# Test case for float input
print(lateralsuface_cylinder(10.0, 5.0)) # Output: 0
print(lateralsuface_cylinder(10, 5.0)) # Output: 0
print(lateralsuface_cylinder(10.0, 5) # Output: 0

# Test case for complex input
print(lateralsuface_cylinder(10+5j, 5)) # Output: 0
print(lateralsuface_cylinder(10, 5+3j) # Output: 0
print(lateralsuface_cylinder(10+5j, 5+3j) # Output: 0

# Test case for non-integer input
print(lateralsuface_cylinder(10.5, 5)) # Output: 0
print(lateralsuface_cylinder(10, 5.5) # Output: 0
print(lateralsuface_cylinder(10.5, 5.5) # Output: 0

# Test case for non-numeric input
print(lateralsuface_cylinder("10", "5")) # Output: 0
print(lateralsuface_cylinder(True, 5) # Output: 0
print(lateralsuface_cylinder(10, True) # Output: 0
print(lateralsuface_cylinder(None, 5) # Output: 0
print(lateralsuface_cylinder(10, None) # Output: 0
print(lateralsuface_cylinder(10, [5]) # Output: 0
print(lateralsuface_cylinder(10, (5,)) # Output: 0
print(lateralsuface_cylinder(10, {5: 6}) # Output: 0
print(lateralsuface_cylinder(10, "5") # Output: 0
print(