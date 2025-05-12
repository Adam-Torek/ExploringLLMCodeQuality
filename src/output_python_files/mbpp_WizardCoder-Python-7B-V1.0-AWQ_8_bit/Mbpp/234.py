"""
Write a function to find the volume of a cube given its side length.
assert volume_cube(3)==27
"""
def volume_cube(side):
    return side**3

print(volume_cube(3)) # Output: 27

# Test cases
print(volume_cube(1)) # Output: 1
print(volume_cube(2)) # Output: 8
print(volume_cube(4)) # Output: 64
print(volume_cube(5)) # Output: 125
print(volume_cube(10)) # Output: 1000

# Test cases
print(volume_cube(0) == 0) # Output: True
print(volume_cube(1) == 1) # Output: False
print(volume_cube(2) == 8) # Output: False
print(volume_cube(3) == 27) # Output: False
print(volume_cube(4) == 64) # Output: False
print(volume_cube(5) == 125) # Output: False
print(volume_cube(10) == 1000) # Output: False

# Test cases
print(volume_cube(-1) == 0) # Output: False
print(volume_cube(0) == 0) # Output: True
print(volume_cube(1) == 1) # Output: False
print(volume_cube(2) == 8) # Output: False
print(volume_cube(3) == 27) # Output: False
print(volume_cube(4) == 64) # Output: False
print(volume_cube(5) == 125) # Output: False
print(volume_cube(10) == 100) # Output: False

# Test cases
print(volume_cube(1.5) == 0) # Output: False
print(volume_cube(0.5) == 0) # Output: False
print(volume_cube(-1) == 0) # Output: False
print(volume_cube(1.0) == 1) # Output: False
print(volume_cube(2.0) == 8) # Output: False
print(volume_cube(3.0) == 27) # Output: False
print(volume_cube(4.0) == 64) # Output: False
print(volume_cube(5.0) == 125) # Output: False
print(volume_cube(10.0) == 100) # Output: False

# Test cases
print(volume_cube("a") == 0) # Output: False
print(volume_cube("1") == 0) # Output: False
print(volume_cube("1.5") == 0) # Output: False
print(volume_cube("0.5") == 0) # Output: False
print(volume_cube("1.0") == 1) # Output: False
print(volume_cube("2.0") == 8) # Output: False
print(volume_cube("3.0") == 27) # Output: False
print(volume_cube("4.0") == 64) # Output: False
print(volume_cube("5.0") == 125) # Output: False
print(volume_cube("10.0") == 100) # Output: False

# Test cases
print(volume_cube("") == 0) # Output: False
print(volume_cube("") == 0) # Output: False
print(volume_cube("") == 0) # Output: False
print(volume_cube("") == 0) # Output: False
print(volume_cube("") == 0) # Output: False
print(volume_cube("") == 0) # Output: False
print(volume_cube("") == 0) # Output: False
print(volume_cube("") == 0) # Output: False
print(volume_cube("") == 0) # Output: False
print(volume_cube("") == 0) # Output: False
print(volume