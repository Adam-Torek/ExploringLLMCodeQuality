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
assert surface_area_sphere(5)==314.1592653589793
"""

def surface_area_sphere(radius):
    return 4*3.141592653589793*radius**2

print(surface_area_sphere(5))

"""
Write a function to find the volume of a sphere given its radius.
assert volume_sphere(5)==523.5987755982989
"""

def volume_sphere(radius):
    return 4/3*3.141592653589793*radius**3

print(volume_sphere(5))

"""
Write a function to find the lateral surface area of a cylinder given its radius and height.
assert lateralsurface_cylinder(5, 5)==314.1592653589793
"""

def lateralsurface_cylinder(radius, height):
    return 2*3.141592653589793*radius*height

print(lateralssurface_cylinder(5, 5))

"""
Write a function to find the volume of a cylinder given its radius and height.
assert volume_cylinder(5, 5)==392.69908169872414
"""

def volume_cylinder(radius, height):
    return 3.141592653589793*radius**2*height

print(volume_cylinder(5, 5))

"""
Write a function to find the lateral surface area of a cone given its radius and height.
assert lateralsurface_cone(5, 5)==157.07963267948966
"""

def lateralsurface_cone(radius, height):
    return 3.141592653589793*radius*(radius+math.sqrt(radius**2+height**2))

print(lateralssurface_cone(5, 5))

"""
Write a function to find the volume of a cone given its radius and height.
assert volume_cone(5, 5)==84.93333333333333
"""

def volume_cone(radius, height):
    return 1/3*3.141592653589793*radius**2*height

print(volume_cone(5, 5))

"""
Write a function to find the lateral surface area of a hemisphere given its radius.
assert lateralsurface_hemisphere(5)==157.07963267948966
"""

def lateralsurface_hemisphere(radius):
    return 3.141592653589793*radius**2

print(lateralssurface_hemisphere(5))

"""
Write a function to find the volume of a hemisphere given its radius.
assert volume_hemisphere(5)==196.34954084936207
"""

def volume_hemisphere(radius):
    return 2/3*3.141592653589793*radius**3

print(volume_hemisphere(5))

"""
Write a function to find the lateral surface area of a pyramid given its base length and height.
assert lateralsurface_pyramid(5, 5)==100
"""

def lateralsurface_pyramid(base, height):