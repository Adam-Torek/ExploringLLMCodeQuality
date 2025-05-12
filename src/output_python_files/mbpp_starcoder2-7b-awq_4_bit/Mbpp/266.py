"""
Write a function to find the lateral surface area of a cube given its side length.
assert lateralsurface_cube(5)==100
"""

def lateralsurface_cube(side):
    return 6*side**2

print(lateralsurface_cube(5))

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
    return 4*3.14*radius**2

print(surface_area_sphere(5))

"""
Write a function to find the volume of a sphere given its radius.
assert volume_sphere(5)==523.5987755982989
"""

def volume_sphere(radius):
    return 4/3*3.14*radius**3

print(volume_sphere(5))

"""
Write a function to find the lateral surface area of a cylinder given its radius and height.
assert lateralsurface_cylinder(5, 10)==314
"""

def lateralsurface_cylinder(radius, height):
    return 2*3.14*radius*height

print(lateralssurface_cylinder(5, 10))

"""
Write a function to find the volume of a cylinder given its radius and height.
assert volume_cylinder(5, 10)==785
"""

def volume_cylinder(radius, height):
    return 3.14*radius**2*height

print(volume_cylinder(5, 10))

"""
Write a function to find the lateral surface area of a cone given its radius and height.
assert lateralsurface_cone(5, 10)==157
"""

def lateralsurface_cone(radius, height):
    return 3.14*radius*(radius+height)

print(lateralssurface_cone(5, 10))

"""
Write a function to find the volume of a cone given its radius and height.
assert volume_cone(5, 10)==84.9
"""

def volume_cone(radius, height):
    return 3.14*radius**2*height/3

print(volume_cone(5, 10))

"""
Write a function to find the lateral surface area of a hemisphere given its radius.
assert lateralsurface_hemisphere(5)==157
"""

def lateralsurface_hemisphere(radius):
    return 3.14*radius**2

print(lateralssurface_hemisphere(5))

"""
Write a function to find the volume of a hemisphere given its radius.
assert volume_hemisphere(5)==196.34954084936207
"""

def volume_hemisphere(radius):
    return 3.14*radius**3/3

print(volume_hemisphere(5))

"""
Write a function to find the lateral surface area of a pyramid given its base side length and height.
assert lateralsurface_pyramid(5, 10)==157
"""

def lateralsurface_pyramid(base, height):
    return 3*base*height

print(lateralssurface_pyramid(5, 10))

"""
Write a function to find the volume of a pyramid given its base side length and height.
assert volume_pyramid(5, 10)==25
"""

def volume_pyramid(base, height):
    return base**2*height/3

print(volume_pyramid(5, 10))

"""