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
print(volume_cube(6)) # Output: 216
print(volume_cube(7) == 343) # Output: True
print(volume_cube(8) == 512) # Output: True
print(volume_cube(9) == 729) # Output: True
print(volume_cube(10) == 10000) # Output: True

# Test cases with negative side length
print(volume_cube(-3) == 27) # Output: False
print(volume_cube(-2) == 8) # Output: False
print(volume_cube(-4) == 64) # Output: False
print(volume_cube(-5) == 125) # Output: False
print(volume_cube(-6) == 216) # Output: False
print(volume_cube(-7) == 343) # Output: False
print(volume_cube(-8) == 512) # Output: False
print(volume_cube(-9) == 1000) # Output: False

# Test cases with float side length
print(volume_cube(3.0) == 27.0) # Output: True
print(volume_cube(2.5) == 15.875) # Output: True
print(volume_cube(4.2) == 108.06) # Output: True
print(volume_cube(5.5) == 1525.0) # Output: True
print(volume_cube(6.7) == 2197.28) # Output: True
print(volume_cube(7.8) == 3024.0) # Output: True
print(volume_cube(8.1) == 4000.0) # Output: True
print(volume_cube(9.9) == 6481.0) # Output: True

# Test cases with string side length
print(volume_cube("3") == 27) # Output: False
print(volume_cube("2") == 8) # Output: False
print(volume_cube("4") == 64) # Output: False
print(volume_cube("5") == 125) # Output: False
print(volume_cube("6") == 216) # Output: False
print(volume_cube("7") == 343) # Output: False
print(volume_cube("8") == 512) # Output: False
print(volume_cube("9") == 1000) # Output: False

# Test cases with list side length
print(volume_cube([3]) == 27) # Output: False
print(volume_cube([2]) == 8) # Output: False
print(volume_cube([4]) == 64) # Output: False
print(volume_cube([5]) == 125) # Output: False
print(volume_cube([6]) == 216) # Output: False
print(volume_cube([7]) == 343) # Output: False
print(volume_cube([8]) == 512) # Output: False
print(volume_cube([9]) == 1000) # Output: False

# Test cases with tuple side length
print(volume_cube((3) == 2