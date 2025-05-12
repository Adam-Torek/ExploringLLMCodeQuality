"""
Write a function to find the lateral surface area of a cube given its side length.
assert lateralsurface_cube(5)==100
"""

def lateralsurface_cube(side):
    return 6*side**2

print(lateral_surface_cube(5))

"""
Write a function to find the volume of a cube given its side length.
assert volume_cube(5)==125
"""

def volume_cube(side):
    return side**3

print(volume_cube(5))

"""
Write a function to find the surface area of a sphere given its radius.
assert surface_area_sphere(5)==157
"""

def surface_area_sphere(radius):
    return 4*pi*radius**2

print(surface_area_sphere(5))

"""
Write a function to find the volume of a sphere given its radius.
assert volume_sphere(5)==523
"""

def volume_sphere(radius):
    return 4/3*pi*radius**3

print(volume_sphere(5))

"""
Write a function to find the lateral surface area of a cylinder given its radius and height.
assert lateralsurface_cylinder(5, 10)==314
"""

def lateralsurface_cylinder(radius, height):
    return 2*pi*radius*height

print(lateral_surface_cylinder(5, 10))

"""
Write a function to find the total surface area of a cylinder given its radius and height.
assert totalsurface_cylinder(5, 10)==628
"""

def totalsurface_cylinder(radius, height):
    return 2*pi*radius*height + 2*pi*radius**2

print(totalsurface_cylinder(5, 10))

"""
Write a function to find the volume of a cylinder given its radius and height.
assert volume_cylinder(5, 10)==785
"""

def volume_cylinder(radius, height):
    return pi*radius**2*height

print(volume_cylinder(5, 10))

"""
Write a function to find the lateral surface area of a cone given its radius and height.
assert lateralsurface_cone(5, 10)==157
"""

def lateralsurface_cone(radius, height):
    return pi*radius*height

print(lateral_surface_cone(5, 10))

"""
Write a function to find the total surface area of a cone given its radius and height.
assert totalsurface_cone(5, 10)==314
"""

def totalsurface_cone(radius, height):
    return pi*radius*height + pi*radius**2

print(totalsurface_cone(5, 10))

"""
Write a function to find the volume of a cone given its radius and height.
assert volume_cone(5, 10)==196
"""

def volume_cone(radius, height):
    return 1/3*pi*radius**2*height

print(volume_cone(5, 10))

"""
Write a function to find the lateral surface area of a pyramid given its base side length and height.
assert lateralsurface_pyramid(5, 10)==157
"""

def lateralsurface_pyramid(base, height):
    return base*height

print(lateral_surface_pyramid(5, 10))

"""
Write a function to find the total surface area of a pyramid given its base side length and height.
assert totalsurface_pyramid(5, 10)==314
"""

def totalsurface_pyramid(base, height):
    return base*height + base**2

print(totalsurface_pyramid(5, 10))

"""
Write a function to find the volume of a pyramid given its base side length and height.
assert volume_pyramid(5, 10)==25
"""

def volume_pyramid(base, height):
    return 1/3*base*height

print(volume_pyramid(5, 10))

"""
Write a function to find the lateral surface area of a rectangular prism given its length, width, and height.
assert lateralsurface_rectangularprism(5,