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
assert surface_area_sphere(5)==314.1592653589793
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
assert lateralsurface_cylinder(5, 10)==314.1592653589793
"""

def lateralsurface_cylinder(radius, height):
    return 2*3.14*radius*height

print(lateral_surface_cylinder(5, 10))

"""
Write a function to find the volume of a cylinder given its radius and height.
assert volume_cylinder(5, 10)==1570.7963267948966
"""

def volume_cylinder(radius, height):
    return 3.14*radius**2*height

print(volume_cylinder(5, 10))

"""
Write a function to find the surface area of a cone given its radius and height.
assert surface_area_cone(5, 10)==235.6194490192345
"""

def surface_area_cone(radius, height):
    return 3.14*radius*(radius+((radius**2+height**2)**0.5))

print(surface_area_cone(5, 10))

"""
Write a function to find the volume of a cone given its radius and height.
assert volume_cone(5, 10)==88.40944267887299
"""

def volume_cone(radius, height):
    return 1/3*3.14*radius**2*height

print(volume_cone(5, 10))

"""
Write a function to find the surface area of a pyramid given its base side length and height.
assert surface_area_pyramid(5, 10)==157.07963267948966
"""

def surface_area_pyramid(base, height):
    return 1/2*base*height

print(surface_area_pyramid(5, 10))

"""
Write a function to find the volume of a pyramid given its base side length and height.
assert volume_pyramid(5, 10)==25.0
"""

def volume_pyramid(base, height):
    return 1/3*base*height

print(volume_pyramid(5, 10))

"""
Write a function to find the surface area of a rectangular prism given its length, width, and height.
assert surface_area_rectangular_prism(5, 10, 15)==1500
"""

def surface_area_rectangular_prism(length, width,