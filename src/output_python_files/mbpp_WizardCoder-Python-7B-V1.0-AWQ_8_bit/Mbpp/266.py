"""
Write a function to find the lateral surface area of a cube given its side length.
assert lateralsurface_cube(5)==100
"""
def lateralsurface_cube(side_length):
    return 6 * side_length ** 2

print(lateralsurface_cube(5)) # Output: 100
print(lateralsurface_cube(10)) # Output: 1000
print(lateralsurface_cube(1)) # Output: 6

# Test cases
print(lateralsurface_cube(5)) # Output: 100
print(lateralsurface_cube(10)) # Output: 1000
print(lateralsurface_cube(1)) # Output: 6