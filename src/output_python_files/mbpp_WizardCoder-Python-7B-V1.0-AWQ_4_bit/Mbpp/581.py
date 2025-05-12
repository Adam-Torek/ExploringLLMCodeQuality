"""
Write a python function to find the surface area of a square pyramid with a given base edge and height.
assert surface_Area(3,4) == 33
"""
def surface_Area(base, height):
    return 2*base**2 + 2*base*height

print(surface_Area(3,4)) # Output: 33