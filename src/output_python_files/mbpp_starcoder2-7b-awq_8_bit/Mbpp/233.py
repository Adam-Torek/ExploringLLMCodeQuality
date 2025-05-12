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
Write a function to find the surface area of a sphere.
assert math.isclose(surface_area_sphere(10), 1256.6370614359172, rel_tol=0.001)
"""

def surface_area_sphere(r):
    return 4*math.pi*r**2

"""
Write a function to find the lateral surface area of a sphere.
assert math.isclose(lateral_surface_area_sphere(10), 628.3185307179586, rel_tol=0.001)
"""

def lateral_surface_area_sphere(r):
    return 4*math.pi*r**2

"""
Write a function to find the volume of a sphere.
assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)
"""

def volume_sphere(r):
    return 4/3*math.pi*r**3

"""
Write a function to find the surface area of a cone.
assert math.isclose(surface_area_cone(10,5), 251.32741228718345, rel_tol=0.001)
"""

def surface_area_cone(r,h):
    return math.pi*r*(r+math.sqrt(r**2+h**2))

"""
Write a function to find the lateral surface area of a cone.
assert math.isclose(lateral_surface_area_cone(10,5), 157.07963267948966, rel_tol=0.001)
"""

def lateral_surface_area_cone(r,h):
    return math.pi*r*math.sqrt(r**2+h**2)

"""
Write a function to find the volume of a cone.
assert math.isclose(volume_cone(10,5), 83.77580409572782, rel_tol=0.001)
"""

def volume_cone(r,h):
    return 1/3*math.pi*r**2*h

"""
Write a function to find the surface area of a hemisphere.
assert math.isclose(surface_area_hemisphere(10), 314.1592653589793, rel_tol=0.001)
"""

def surface_area_hemisphere(r):
    return 3*math.pi*r**2

"""
Write a function to find the lateral surface area of a hemisphere.
assert math.isclose(lateral_surface_area_hemisphere(10), 251.32741228718345, rel_tol=0.001)
"""

def lateral_surface_area_hemisphere(r):
    return 2*math.pi*r**2

"""
Write a function to find the volume of a hemisphere.
assert math.isclose(volume_hemisphere(10), 251.32741228718345, rel_tol=0.001)
"""

def volume_hemisphere(r):
    return 2/3*