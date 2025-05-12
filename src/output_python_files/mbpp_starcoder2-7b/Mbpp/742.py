"""
Write a function to caluclate the area of a tetrahedron.
assert area_tetrahedron(3)==15.588457268119894
"""

def area_tetrahedron(a):
    return (a**2)*((3**0.5)/4)

print(area_tetrahedron(3))

"""
Write a function to calculate the volume of a tetrahedron.
assert volume_tetrahedron(3)==13.416407864998739
"""

def volume_tetrahedron(a):
    return (a**3)*((3**0.5)/12)

print(volume_tetrahedron(3))

"""
Write a function to calculate the surface area of a tetrahedron.
assert surface_area_tetrahedron(3)==39.47841760435743
"""

def surface_area_tetrahedron(a):
    return (a**2)*((3**0.5)/2)

print(surface_area_tetrahedron(3))

"""
Write a function to calculate the volume of a cube.
assert volume_cube(3)==27
"""

def volume_cube(a):
    return a**3

print(volume_cube(3))

"""
Write a function to calculate the surface area of a cube.
assert surface_area_cube(3)==54
"""

def surface_area_cube(a):
    return 6*a**2

print(surface_area_cube(3))

"""
Write a function to calculate the volume of a sphere.
assert volume_sphere(3)==113.09733552923255
"""

def volume_sphere(a):
    return (4/3)*3.14*(a**3)

print(volume_sphere(3))

"""
Write a function to calculate the surface area of a sphere.
assert surface_area_sphere(3)==113.09733552923255
"""

def surface_area_sphere(a):
    return 4*3.14*(a**2)

print(surface_area_sphere(3))

"""
Write a function to calculate the volume of a cone.
assert volume_cone(3, 4)==26.194444444444445
"""

def volume_cone(r, h):
    return (1/3)*3.14*(r**2)*h

print(volume_cone(3, 4))

"""
Write a function to calculate the surface area of a cone.
assert surface_area_cone(3, 4)==56.54866776461627
"""

def surface_area_cone(r, h):
    return 3.14*(r**2)+(3.14*r*h)

print(surface_area_cone(3, 4))

"""
Write a function to calculate the volume of a cylinder.
assert volume_cylinder(3, 4)==36.0
"""

def volume_cylinder(r, h):
    return 3.14*(r**2)*h

print(volume_cylinder(3, 4))

"""
Write a function to calculate the surface area of a cylinder.
assert surface_area_cylinder(3, 4)==88.2
"""

def surface_area_cylinder(r, h):
    return 2*3.14*(r**2)+2*3.14*r*h

print(surface_area_cylinder(3, 4))

"""
Write a function to calculate the volume of a pyramid.
assert volume_pyramid(3, 4)==12.0
"""

def volume_pyramid(b, h):
    return (1/3)*b*h

print(volume_pyramid(3, 4