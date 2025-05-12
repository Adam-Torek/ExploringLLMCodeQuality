"""
Write a function to find the surface area of a cylinder.
assert surfacearea_cylinder(10,5)==942.45
"""
def surfacearea_cylinder(r,h):
    return 2*3.14*r*h+2*3.14*r**2

"""
Write a function to find the volume of a cylinder.
assert volume_cylinder(10,5)==1570.79
"""
def volume_cylinder(r,h):
    return 3.14*r**2*h

"""
Write a function to find the surface area of a sphere.
assert surfacearea_sphere(10)==1256.64
"""
def surfacearea_sphere(r):
    return 4*3.14*r**2

"""
Write a function to find the volume of a sphere.
assert volume_sphere(10)==4188.79
"""
def volume_sphere(r):
    return 4/3*3.14*r**3

"""
Write a function to find the surface area of a cone.
assert surfacearea_cone(10,5)==157.079
"""
def surfacearea_cone(r,h):
    return 3.14*r*(r+math.sqrt(h**2+r**2))

"""
Write a function to find the volume of a cone.
assert volume_cone(10,5)==83.775
"""
def volume_cone(r,h):
    return 1/3*3.14*r**2*h

"""
Write a function to find the surface area of a cube.
assert surfacearea_cube(10)==600
"""
def surfacearea_cube(a):
    return 6*a**2

"""
Write a function to find the volume of a cube.
assert volume_cube(10)==1000
"""
def volume_cube(a):
    return a**3

"""
Write a function to find the surface area of a cuboid.
assert surfacearea_cuboid(10,5,2)==100
"""
def surfacearea_cuboid(l,b,h):
    return 2*(l*b+b*h+h*l)

"""
Write a function to find the volume of a cuboid.
assert volume_cuboid(10,5,2)==100
"""
def volume_cuboid(l,b,h):
    return l*b*h

"""
Write a function to find the surface area of a hemisphere.
assert surfacearea_hemisphere(10)==314.159
"""
def surfacearea_hemisphere(r):
    return 3*3.14*r**2

"""
Write a function to find the volume of a hemisphere.
assert volume_hemisphere(10)==1570.79
"""
def volume_hemisphere(r):
    return 2/3*3.14*r**3

"""
Write a function to find the surface area of a torus.
assert surfacearea_torus(10,5)==1256.64
"""
def surfacearea_torus(r,R):
    return 4*3.14*r*R

"""
Write a function to find the volume of a torus.
assert volume_torus(10,5)==4188.79
"""
def volume_torus(r,R):
    return 2*3.14*r**2*R

"""
Write a function to find the surface area of a rectangular prism.
assert surfacearea_rectangularprism(10,5,2)==100
"""
def surfacearea_rectangularprism(l,b,h):
    return 2*(l*b+b*h+h*l)

"""
Write a function to find the volume of a rectangular prism.
assert volume_rectangularprism(10,5,2)==100
"""
def volume_rectangularprism(l,b,h):
    return l*b*h

"""
Write a function to find the surface area of a triangular prism.
assert surfacearea_triangularprism(10,5,2)==100
"""
def surfacearea_tri