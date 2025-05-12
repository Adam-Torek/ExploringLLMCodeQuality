"""
Write a function to find the lateral surface area of a cone given radius r and the height h.
assert lateralsurface_cone(5,12)==204.20352248333654
"""

def lateralsurface_cone(r,h):
    return math.pi*r*(r+math.sqrt(h**2+r**2))

print(lateralsurface_cone(5,12))

"""
Write a function to find the volume of a cone given radius r and the height h.
assert volume_cone(5,12)==176.71458676442586
"""

def volume_cone(r,h):
    return (1/3)*math.pi*r**2*h

print(volume_cone(5,12))

"""
Write a function to find the surface area of a sphere given radius r.
assert surface_sphere(5)==153.93804002589985
"""

def surface_sphere(r):
    return 4*math.pi*r**2

print(surface_sphere(5))

"""
Write a function to find the lateral surface area of a sphere given radius r.
assert lateralsurface_sphere(5)==100.79644737231007
"""

def lateralsurface_sphere(r):
    return 4*math.pi*r**2

print(lateralsurface_sphere(5))

"""
Write a function to find the volume of a sphere given radius r.
assert volume_sphere(5)==523.5987755982989
"""

def volume_sphere(r):
    return (4/3)*math.pi*r**3

print(volume_sphere(5))

"""
Write a function to find the surface area of a cylinder given radius r and height h.
assert surface_cylinder(5,12)==376.9911184307752
"""

def surface_cylinder(r,h):
    return 2*math.pi*r*(r+h)

print(surface_cylinder(5,12))

"""
Write a function to find the lateral surface area of a cylinder given radius r and height h.
assert lateralsurface_cylinder(5,12)==376.9911184307752
"""

def lateralsurface_cylinder(r,h):
    return 2*math.pi*r*h

print(lateralsurface_cylinder(5,12))

"""
Write a function to find the volume of a cylinder given radius r and height h.
assert volume_cylinder(5,12)==376.9911184307752
"""

def volume_cylinder(r,h):
    return math.pi*r**2*h

print(volume_cylinder(5,12))

"""
Write a function to find the surface area of a cube given side s.
assert surface_cube(5)==150
"""

def surface_cube(s):
    return 6*s**2

print(surface_cube(5))

"""
Write a function to find the lateral surface area of a cube given side s.
assert lateralsurface_cube(5)==120
"""

def lateralsurface_cube(s):
    return 4*s**2

print(lateralsurface_cube(5))

"""
Write a function to find the volume of a cube given side s.
assert volume_cube(5)==125
"""

def volume_cube(s):
    return s**3

print(volume_cube(5))

"""
Write a function to find the surface area of a rectangular prism given length l, width w and height h.
assert surface_rectangularprism(5,12,10)==1320
"""

def surface_rectangularprism(l,w,h):
    return 2*(l*w+l*h+w*h)

print(surface_rectangularprism(5,12,10))

"""
Write a function to find the lateral surface area of