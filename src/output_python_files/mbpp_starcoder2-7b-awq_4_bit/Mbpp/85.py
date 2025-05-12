"""
Write a function to find the surface area of a sphere.
assert math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001)
"""

def surfacearea_sphere(radius):
    return 4 * math.pi * radius ** 2

assert math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001)

"""
Write a function to find the volume of a sphere.
assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)
"""

def volume_sphere(radius):
    return (4 / 3) * math.pi * radius ** 3

assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)

"""
Write a function to find the volume of a cylinder.
assert math.isclose(volume_cylinder(10, 10), 31415.92653589793, rel_tol=0.001)
"""

def volume_cylinder(radius, height):
    return math.pi * radius ** 2 * height

assert math.isclose(volume_cylinder(10, 10), 31415.92653589793, rel_tol=0.001)

"""
Write a function to find the surface area of a cylinder.
assert math.isclose(surfacearea_cylinder(10, 10), 1256.6370614359173, rel_tol=0.001)
"""

def surfacearea_cylinder(radius, height):
    return 2 * math.pi * radius * (radius + height)

assert math.isclose(surfacearea_cylinder(10, 10), 1256.6370614359173, rel_tol=0.001)

"""
Write a function to find the volume of a cone.
assert math.isclose(volume_cone(10, 10), 1047.1975511965976, rel_tol=0.001)
"""

def volume_cone(radius, height):
    return (1 / 3) * math.pi * radius ** 2 * height

assert math.isclose(volume_cone(10, 10), 1047.1975511965976, rel_tol=0.001)

"""
Write a function to find the surface area of a cone.
assert math.isclose(surfacearea_cone(10, 10), 216.7135706092186, rel_tol=0.001)
"""

def surfacearea_cone(radius, height):
    return math.pi * radius * (radius + math.sqrt(radius ** 2 + height ** 2))

assert math.isclose(surfacearea_cone(10, 10), 216.7135706092186, rel_tol=0.001)

"""
Write a function to find the volume of a cube.
assert math.isclose(volume_cube(10), 1000, rel_tol=0.001)
"""

def volume_cube(side):
    return side ** 3

assert math.isclose(volume_cube(10), 1000, rel_tol=0.001)

"""
Write a function to find the surface area of a cube.
assert math.isclose(surfacearea_cube(10), 600, rel_tol=0.001)
"""

def surfacearea_cube(side):
    return 6 * side ** 2

assert math.isclose(surfacearea_cube(10), 6