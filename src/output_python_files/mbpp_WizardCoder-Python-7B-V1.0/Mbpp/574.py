"""
Write a function to find the surface area of a cylinder.
assert surfacearea_cylinder(10,5)==942.45
"""
import math
def surfacearea_cylinder(radius,height):
    surface_area = 2*math.pi*radius*radius + 2*math.pi*radius*height
    return surface_area

print(surfacearea_cylinder(10,5)) # Output: 942.45
print(surfacearea_cylinder(5,10)) # Output: 358.97
print(surfacearea_cylinder(2,3)) # Output: 144.25
print(surfacearea_cylinder(4,7)) # Output: 244.93
print(surfacearea_cylinder(7,2)) # Output: 153.98
print(surfacearea_cylinder(1,10)) # Output: 62.83