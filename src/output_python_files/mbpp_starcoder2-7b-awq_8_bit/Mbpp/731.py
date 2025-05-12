"""
Write a function to find the lateral surface area of a cone given radius r and the height h.
assert lateralsurface_cone(5,12)==204.20352248333654
"""

def lateralsurface_cone(r,h):
    return math.pi*r*(r+math.sqrt(r**2+h**2))

print(lateralsurface_cone(5,12))

"""
Write a function to find the volume of a cone given radius r and the height h.
assert volume_cone(5,12)==84.90450849876903
"""

def volume_cone(r,h):
    return (1/3)*math.pi*r**2*h

print(volume_cone(5,12))

"""
Write a function to find the surface area of a cylinder given radius r and the height h.
assert surface_cylinder(5,12)==157.07963267948966
"""

def surface_cylinder(r,h):
    return 2*math.pi*r*(r+h)

print(surface_cylinder(5,12))

"""
Write a function to find the lateral surface area of a cylinder given radius r and the height h.
assert lateralsurface_cylinder(5,12)==314.1592653589793
"""

def lateralsurface_cylinder(r,h):
    return 2*math.pi*r*h

print(lateralssurface_cylinder(5,12))

"""
Write a function to find the volume of a cylinder given radius r and the height h.
assert volume_cylinder(5,12)==3141.592653589793
"""

def volume_cylinder(r,h):
    return math.pi*r**2*h

print(volume_cylinder(5,12))

"""
Write a function to find the surface area of a sphere given radius r.
assert surface_sphere(5)==157.07963267948966
"""

def surface_sphere(r):
    return 4*math.pi*r**2

print(surface_sphere(5))

"""
Write a function to find the lateral surface area of a sphere given radius r.
assert lateralsurface_sphere(5)==157.07963267948966
"""

def lateralsurface_sphere(r):
    return 4*math.pi*r**2

print(lateralssurface_sphere(5))

"""
Write a function to find the volume of a sphere given radius r.
assert volume_sphere(5)==523.5987755982989
"""

def volume_sphere(r):
    return (4/3)*math.pi*r**3

print(volume_sphere(5))

"""
Write a function to find the surface area of a hemisphere given radius r.
assert surface_hemisphere(5)==157.07963267948966
"""

def surface_hemisphere(r):
    return 3*math.pi*r**2

print(surface_hemisphere(5))

"""
Write a function to find the lateral surface area of a hemisphere given radius r.
assert lateralsurface_hemisphere(5)==157.07963267948966
"""

def lateralsurface_hemisphere(r):
    return 3*math.pi*r**2

print(lateralssurface_hemisphere(5))

"""
Write a function to find the volume of a hemisphere given radius r.
assert volume_hemisphere(5)==196.34954084936207
"""

def volume_hemisphere(r):
    return (2/3)*math.pi*r**3

print(volume_hemisphere(5))

"""
Write a function to find the surface area of a truncated cone given radius r1, radius