"""
Write a function to find the surface area of a cylinder.
assert surfacearea_cylinder(10,5)==942.45
"""

def surfacearea_cylinder(r,h):
    return 2*3.14*r*h+2*3.14*r**2

print(surfacearea_cylinder(10,5))

"""
Write a function to find the volume of a cylinder.
assert volume_cylinder(10,5)==1570.79
"""

def volume_cylinder(r,h):
    return 3.14*r**2*h

print(volume_cylinder(10,5))

"""
Write a function to find the surface area of a sphere.
assert surfacearea_sphere(10)==1256.64
"""

def surfacearea_sphere(r):
    return 4*3.14*r**2

print(surfacearea_sphere(10))

"""
Write a function to find the volume of a sphere.
assert volume_sphere(10)==4188.79
"""

def volume_sphere(r):
    return 4/3*3.14*r**3

print(volume_sphere(10))

"""
Write a function to find the surface area of a cone.
assert surfacearea_cone(10,5)==235.62
"""

def surfacearea_cone(r,h):
    return 3.14*r*(r+((r**2+h**2)**0.5))

print(surfacearea_cone(10,5))

"""
Write a function to find the volume of a cone.
assert volume_cone(10,5)==837.75
"""

def volume_cone(r,h):
    return 1/3*3.14*r**2*h

print(volume_cone(10,5))

"""
Write a function to find the surface area of a cube.
assert surfacearea_cube(10)==600
"""

def surfacearea_cube(a):
    return 6*a**2

print(surfacearea_cube(10))

"""
Write a function to find the volume of a cube.
assert volume_cube(10)==1000
"""

def volume_cube(a):
    return a**3

print(volume_cube(10))

"""
Write a function to find the surface area of a cuboid.
assert surfacearea_cuboid(10,5,2)==1000
"""

def surfacearea_cuboid(l,b,h):
    return 2*(l*b+b*h+h*l)

print(surfacearea_cuboid(10,5,2))

"""
Write a function to find the volume of a cuboid.
assert volume_cuboid(10,5,2)==100
"""

def volume_cuboid(l,b,h):
    return l*b*h

print(volume_cuboid(10,5,2))

"""
Write a function to find the surface area of a hemisphere.
assert surfacearea_hemisphere(10)==1570.79
"""

def surfacearea_hemisphere(r):
    return 3*3.14*r**2

print(surfacearea_hemisphere(10))

"""
Write a function to find the volume of a hemisphere.
assert volume_hemisphere(10)==2680.48
"""

def volume_hemisphere(r):
    return 2/3*3.14*r**3

print(volume_hemisphere(10))

"""
Write a function to find the surface area of a torus.
assert surfacearea_torus(10,5)==1256.64
"""

def surfacearea_torus(r,R):
    return 2*3.14*r*R+2*3.14*r**2

print(surfacearea_torus(10,5))

"""