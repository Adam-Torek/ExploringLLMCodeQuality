"""
Write a function to find the circumference of a circle.
assert math.isclose(circle_circumference(10), 62.830000000000005, rel_tol=0.001)
"""

def circle_circumference(radius):
    return 2 * math.pi * radius

assert math.isclose(circle_circumference(10), 62.830000000000005, rel_tol=0.001)

"""
Write a function to find the area of a circle.
assert math.isclose(circle_area(10), 314.1592653589793, rel_tol=0.001)
"""

def circle_area(radius):
    return math.pi * radius ** 2

assert math.isclose(circle_area(10), 314.1592653589793, rel_tol=0.001)

"""
Write a function to find the volume of a sphere.
assert math.isclose(sphere_volume(10), 4188.790204786391, rel_tol=0.001)
"""

def sphere_volume(radius):
    return 4 / 3 * math.pi * radius ** 3

assert math.isclose(sphere_volume(10), 4188.790204786391, rel_tol=0.001)

"""
Write a function to find the surface area of a sphere.
assert math.isclose(sphere_surface_area(10), 1256.6370614359172, rel_tol=0.001)
"""

def sphere_surface_area(radius):
    return 4 * math.pi * radius ** 2

assert math.isclose(sphere_surface_area(10), 1256.6370614359172, rel_tol=0.001)

"""
Write a function to find the volume of a cylinder.
assert math.isclose(cylinder_volume(10, 10), 3141.592653589793, rel_tol=0.001)
"""

def cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height

assert math.isclose(cylinder_volume(10, 10), 3141.592653589793, rel_tol=0.001)

"""
Write a function to find the surface area of a cylinder.
assert math.isclose(cylinder_surface_area(10, 10), 1256.6370614359172, rel_tol=0.001)
"""

def cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * height + 2 * math.pi * radius ** 2

assert math.isclose(cylinder_surface_area(10, 10), 1256.6370614359172, rel_tol=0.001)

"""
Write a function to find the volume of a cone.
assert math.isclose(cone_volume(10, 10), 1047.1975511965976, rel_tol=0.001)
"""

def cone_volume(radius, height):
    return 1 / 3 * math.pi * radius ** 2 * height

assert math.isclose(cone_volume(10, 10), 1047.1975511965976, rel_tol=0.001)

"""
Write a function to find the surface area of a cone.
assert math.isclose(cone_surface_area(10, 10), 211.3172424080821, rel_tol=0.0