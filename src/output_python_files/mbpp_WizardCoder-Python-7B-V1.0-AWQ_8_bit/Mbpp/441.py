"""
Write a function to find the surface area of a cube of a given size.
assert surfacearea_cube(5)==150
"""
def surfacearea_cube(size):
    return 6 * size ** 2

print(surfacearea_cube(5)) # Output: 150
print(surfacearea_cube(10)) # Output: 1000
print(surfacearea_cube(1)) # Output: 6

# Test cases
print(surfacearea_cube(5)) # Output: 150
print(surfacearea_cube(10)) # Output: 1000
print(surfacearea_cube(1)) # Output: 6