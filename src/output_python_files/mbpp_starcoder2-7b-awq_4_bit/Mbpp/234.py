"""
Write a function to find the volume of a cube given its side length.
assert volume_cube(3)==27
"""

def volume_cube(side_length):
    return side_length**3

print(volume_cube(3))

"""
Write a function to find the volume of a sphere given its radius.
assert volume_sphere(3)==113.09733552923255
"""

def volume_sphere(radius):
    return (4/3)*3.14*radius**3

print(volume_sphere(3))

"""
Write a function to find the volume of a cylinder given its radius and height.
assert volume_cylinder(3, 5)==141.37166941154066
"""

def volume_cylinder(radius, height):
    return 3.14*radius**2*height

print(volume_cylinder(3, 5))

"""
Write a function to find the volume of a cone given its radius and height.
assert volume_cone(3, 5)==47.12388980384689
"""

def volume_cone(radius, height):
    return 3.14*radius**2*height/3

print(volume_cone(3, 5))

"""
Write a function to find the volume of a pyramid given its base and height.
assert volume_pyramid(3, 5)==7.5
"""

def volume_pyramid(base, height):
    return (base**2*height)/3

print(volume_pyramid(3, 5))

"""
Write a function to find the volume of a rectangular prism given its length, width, and height.
assert volume_rectangular_prism(3, 5, 7)==105
"""

def volume_rectangular_prism(length, width, height):
    return length*width*height

print(volume_rectangular_prism(3, 5, 7))

"""
Write a function to find the volume of a triangular prism given its base, height, and width.
assert volume_triangular_prism(3, 5, 7)==105
"""

def volume_triangular_prism(base, height, width):
    return (base*height*width)/2

print(volume_triangular_prism(3, 5, 7))

"""
Write a function to find the volume of a sphere given its radius.
assert volume_sphere(3)==113.09733552923255
"""

def volume_sphere(radius):
    return (4/3)*3.14*radius**3

print(volume_sphere(3))

"""
Write a function to find the volume of a cylinder given its radius and height.
assert volume_cylinder(3, 5)==141.37166941154066
"""

def volume_cylinder(radius, height):
    return 3.14*radius**2*height

print(volume_cylinder(3, 5))

"""
Write a function to find the volume of a cone given its radius and height.
assert volume_cone(3, 5)==47.12388980384689
"""

def volume_cone(radius, height):
    return 3.14*radius**2*height/3

print(volume_cone(3, 5))

"""
Write a function to find the volume of a pyramid given its base and height.
assert volume_pyramid(3, 5)==7.5
"""

def volume_pyramid(base, height):
    return (base**2*height)/3

print(volume_pyramid(3, 5))

"""
Write a function to find the volume of a rectangular prism given its length, width, and height.
assert volume_rectangular_prism(3, 5, 7)==105