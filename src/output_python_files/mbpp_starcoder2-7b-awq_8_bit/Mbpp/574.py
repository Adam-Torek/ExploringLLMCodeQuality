"""
Write a function to find the surface area of a cylinder.
assert surfacearea_cylinder(10,5)==942.45
"""
def surfacearea_cylinder(r,h):
    return 2*3.14*r*h+2*3.14*r**2

"""
Write a function to find the volume of a cylinder.
assert volume_cylinder(10,5)==1570.796
"""
def volume_cylinder(r,h):
    return 3.14*r**2*h

"""
Write a function to find the surface area of a sphere.
assert surfacearea_sphere(10)==1256.637
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
assert surfacearea_cone(10,5)==157.0796
"""
def surfacearea_cone(r,h):
    return 3.14*r*(r+math.sqrt(r**2+h**2))

"""
Write a function to find the volume of a cone.
assert volume_cone(10,5)==83.7759
"""
def volume_cone(r,h):
    return 1/3*3.14*r**2*h

"""
Write a function to find the surface area of a cube.
assert surfacearea_cube(10)==60
"""
def surfacearea_cube(s):
    return 6*s**2

"""
Write a function to find the volume of a cube.
assert volume_cube(10)==1000
"""
def volume_cube(s):
    return s**3

"""
Write a function to find the surface area of a rectangular prism.
assert surfacearea_rectangularprism(10,5,2)==140
"""
def surfacearea_rectangularprism(l,w,h):
    return 2*(l*w+w*h+h*l)

"""
Write a function to find the volume of a rectangular prism.
assert volume_rectangularprism(10,5,2)==100
"""
def volume_rectangularprism(l,w,h):
    return l*w*h

"""
Write a function to find the surface area of a triangular prism.
assert surfacearea_triangularprism(10,5,2)==120
"""
def surfacearea_triangularprism(b,h,l):
    return 2*(b*h+h*l+l*b)

"""
Write a function to find the volume of a triangular prism.
assert volume_triangularprism(10,5,2)==100
"""
def volume_triangularprism(b,h,l):
    return b*h*l

"""
Write a function to find the surface area of a right circular cylinder.
assert surfacearea_rightcircularcylinder(10,5)==157.0796
"""
def surfacearea_rightcircularcylinder(r,h):
    return 2*3.14*r*h+2*3.14*r**2

"""
Write a function to find the volume of a right circular cylinder.
assert volume_rightcircularcylinder(10,5)==83.7759
"""
def volume_rightcircularcylinder(r,h):
    return 3.14*r**2*h

"""
Write a function to find the surface area of a right circular cone.
assert surfacearea_rightcircularcone(10,5)==157.0796
"""
def surfacearea_rightcircularcone(r,h):
    return 3.14*r*(r+math.sqrt(r**2+h**2))

"""
Write a function to find the volume of a right circular cone.
assert volume_rightcircularcone(10,5)==83.7759
"""
def volume_rightcircularcone(r,h):
    return 1/3