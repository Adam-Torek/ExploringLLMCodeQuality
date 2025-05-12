"""
Write a function to find the surface area of a cylinder.
assert surfacearea_cylinder(10,5)==942.45
"""
def surfacearea_cylinder(radius,height):
    import math
    return 2*math.pi*radius*height + 2*math.pi*radius**2

print(surfacearea_cylinder(10,5)) # Output: 942.45