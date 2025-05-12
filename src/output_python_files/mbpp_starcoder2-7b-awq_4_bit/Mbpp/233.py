"""
Write a function to find the lateral surface area of a cylinder.
assert math.isclose(lateralsuface_cylinder(10,5), 314.15000000000003, rel_tol=0.001)
"""

def lateralsuface_cylinder(r,h):
    return 2*math.pi*r*h

"""
Write a function to find the volume of a cylinder.
assert math.isclose(volume_cylinder(10,5), 1570.7963267948966, rel_tol=0.001)
"""

def volume_cylinder(r,h):
    return math.pi*r**2*h

"""
Write a function to find the surface area of a cone.
assert math.isclose(surface_cone(10,5), 314.15000000000003, rel_tol=0.001)
"""

def surface_cone(r,h):
    return math.pi*r*(r+math.sqrt(r**2+h**2))

"""
Write a function to find the lateral surface area of a cone.
assert math.isclose(lateralsuface_cone(10,5), 314.15000000000003, rel_tol=0.001)
"""

def lateralsuface_cone(r,h):
    return math.pi*r*math.sqrt(r**2+h**2)

"""
Write a function to find the volume of a cone.
assert math.isclose(volume_cone(10,5), 1570.7963267948966, rel_tol=0.001)
"""

def volume_cone(r,h):
    return math.pi*r**2*h/3

"""
Write a function to find the surface area of a sphere.
assert math.isclose(surface_sphere(10), 1256.6370614359172, rel_tol=0.001)
"""

def surface_sphere(r):
    return 4*math.pi*r**2

"""
Write a function to find the lateral surface area of a sphere.
assert math.isclose(lateralsuface_sphere(10), 1256.6370614359172, rel_tol=0.001)
"""

def lateralsuface_sphere(r):
    return 4*math.pi*r**2

"""
Write a function to find the volume of a sphere.
assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)
"""

def volume_sphere(r):
    return 4*math.pi*r**3/3

"""
Write a function to find the surface area of a hemisphere.
assert math.isclose(surface_hemisphere(10), 985.3981633974483, rel_tol=0.001)
"""

def surface_hemisphere(r):
    return 3*math.pi*r**2

"""
Write a function to find the lateral surface area of a hemisphere.
assert math.isclose(lateralsuface_hemisphere(10), 985.3981633974483, rel_tol=0.001)
"""

def lateralsuface_hemisphere(r):
    return 3*math.pi*r**2

"""
Write a function to find the volume of a hemisphere.
assert math.isclose(volume_hemisphere(10), 2680.4778614285714, rel_tol=0.001)
"""

def volume_hemisphere(r):
    return 2*math.