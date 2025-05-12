"""
Write a function to find the surface area of a cylinder.
assert surfacearea_cylinder(10,5)==942.45
"""

def surfacearea_cylinder(r,h):
    return 2*3.14*r*h+2*3.14*r**2

print(surfacearea_cylinder(10,5))

"""
Write a function to find the volume of a cylinder.
assert volume_cylinder(10,5)==1570.796
"""

def volume_cylinder(r,h):
    return 3.14*r**2*h

print(volume_cylinder(10,5))

"""
Write a function to find the surface area of a sphere.
assert surfacearea_sphere(10)==1256.637
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
assert surfacearea_cone(10,5)==1717.985
"""

def surfacearea_cone(r,h):
    return 3.14*r*(r+math.sqrt(r**2+h**2))

print(surfacearea_cone(10,5))

"""
Write a function to find the volume of a cone.
assert volume_cone(10,5)==837.758
"""

def volume_cone(r,h):
    return 1/3*3.14*r**2*h

print(volume_cone(10,5))

"""
Write a function to find the surface area of a cube.
assert surfacearea_cube(10)==600
"""

def surfacearea_cube(s):
    return 6*s**2

print(surfacearea_cube(10))

"""
Write a function to find the volume of a cube.
assert volume_cube(10)==1000
"""

def volume_cube(s):
    return s**3

print(volume_cube(10))

"""
Write a function to find the surface area of a rectangular prism.
assert surfacearea_rectangularprism(10,5,2)==1400
"""

def surfacearea_rectangularprism(l,w,h):
    return 2*(l*w+w*h+h*l)

print(surfacearea_rectangularprism(10,5,2))

"""
Write a function to find the volume of a rectangular prism.
assert volume_rectangularprism(10,5,2)==1000
"""

def volume_rectangularprism(l,w,h):
    return l*w*h

print(volume_rectangularprism(10,5,2))

"""
Write a function to find the surface area of a triangular prism.
assert surfacearea_triangularprism(10,5,2)==1400
"""

def surfacearea_triangularprism(b,h,l):
    return 2*(b*h+h*l+l*b)

print(surfacearea_triangularprism(10,5,2))

"""
Write a function to find the volume of a triangular prism.
assert volume_triangularprism(10,5,2)==1000
"""

def volume_triangularprism(b,h,l):
    return b*h*l

print(volume_triangularprism(10,5,2))

"""
Write a function to find the surface area of a hemisphere.
assert surfacearea_hemisphere(10)==1570.796
"""

def surfacearea_hemisphere(r):
    return 3*3.14*r