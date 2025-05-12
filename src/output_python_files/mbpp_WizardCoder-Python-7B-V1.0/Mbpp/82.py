"""
Write a function to find the volume of a sphere.
assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)
"""
import math

def volume_sphere(radius):
    return (4/3) * math.pi * (radius ** 3)

# Test the function with a radius of 10
print(volume_sphere(10))

# Test the function with a radius of 5
print(volume_sphere(5))

# Test the function with a radius of 2.5
print(volume_sphere(2.5))

# Test the function with a radius of 0
print(volume_sphere(0))

# Test the function with a radius of -5
print(volume_sphere(-5))

# Test the function with a radius of 3.14
print(volume_sphere(3.14))

# Test the function with a radius of 3.14159
print(volume_sphere(3.14159))

# Test the function with a radius of 3.141592653589793238462643383279502884197169399375
print(volume_sphere(3.141592653589793238462643383279502884197169399375))

# Test the function with a radius of 3.1415926535897932384626433832795028841971693993755
print(volume_sphere(3.1415926535897932384626433832795028841971693993755))

# Test the function with a radius of 3.14159265358979323846264338327950288419716939937555
print(volume_sphere(3.14159265358979323846264338327950288419716939937555))

# Test the function with a radius of 3.141592653589793238462643383279502884197169399375555
print(volume_sphere(3.14159265358979323846264338327950288419716939937555))

# Test the function with a radius of 3.1415926535897932384626433832795028841971693993755555
print(volume_sphere(3.141592653589793238462643383279502884197169399375555))

# Test the function with a radius of 3.14159265358979323846264338327950288419716939937555555
print(volume_sphere(3.1415926535897932384626433832795028841971693993755555))