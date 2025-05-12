"""
Write a function to find the lateral surface area of a cone given radius r and the height h.
assert lateralsurface_cone(5,12)==204.20352248333654
"""

def lateralsurface_cone(r,h):
    return 3.14*r*(r+math.sqrt(r**2+h**2))

print(lateralsurface_cone(5,12))

"""
Write a function to find the volume of a cone given radius r and the height h.
assert volume_cone(5,12)==83.77580409572781
"""

def volume_cone(r,h):
    return 3.14*r**2*h/3

print(volume_cone(5,12))

"""
Write a function to find the volume of a sphere given radius r.
assert volume_sphere(5)==523.5987755982989
"""

def volume_sphere(r):
    return 4/3*3.14*r**3

print(volume_sphere(5))

"""
Write a function to find the lateral surface area of a sphere given radius r.
assert lateralsurface_sphere(5)==314.1592653589793
"""

def lateralsurface_sphere(r):
    return 4*3.14*r**2

print(lateralsurface_sphere(5))

"""
Write a function to find the total surface area of a sphere given radius r.
assert totalsurface_sphere(5)==1256.6370614359173
"""

def totalsurface_sphere(r):
    return 4*3.14*r**2+4*3.14*r**2

print(totalsurface_sphere(5))

"""
Write a function to find the total surface area of a cylinder given radius r and height h.
assert totalsurface_cylinder(5,12)==1256.6370614359173
"""

def totalsurface_cylinder(r,h):
    return 2*3.14*r**2+2*3.14*r*h

print(totalsurface_cylinder(5,12))

"""
Write a function to find the lateral surface area of a cylinder given radius r and height h.
assert lateralsurface_cylinder(5,12)==1256.6370614359173
"""

def lateralsurface_cylinder(r,h):
    return 2*3.14*r*h

print(lateralsurface_cylinder(5,12))

"""
Write a function to find the volume of a cylinder given radius r and height h.
assert volume_cylinder(5,12)==83.77580409572781
"""

def volume_cylinder(r,h):
    return 3.14*r**2*h

print(volume_cylinder(5,12))

"""
Write a function to find the lateral surface area of a cube given side s.
assert lateralsurface_cube(5)==100
"""

def lateralsurface_cube(s):
    return 6*s**2

print(lateralsurface_cube(5))

"""
Write a function to find the total surface area of a cube given side s.
assert totalsurface_cube(5)==200
"""

def totalsurface_cube(s):
    return 6*s**2

print(totalsurface_cube(5))

"""
Write a function to find the volume of a cube given side s.
assert volume_cube(5)==125
"""

def volume_cube(s):
    return s**3

print(volume_cube(5))

"""
Write a function to find the lateral surface area of a cuboid given length l, width w and height h.
assert