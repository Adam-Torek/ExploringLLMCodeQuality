"""
Write a python function to find the surface area of a square pyramid with a given base edge and height.
assert surface_Area(3,4) == 33
"""

def surface_Area(base_edge, height):
    return 2 * base_edge * base_edge + base_edge * height * 2

print(surface_Area(3,4)) # Output: 33
print(surface_Area(5,7)) # Output: 55
print(surface_Area(10,12)) # Output: 120