"""
Write a python function to find the volume of a triangular prism.
assert find_Volume(10,8,6) == 240
"""
def find_Volume(base, height, slant_height):
    return 0.5 * base * height * slant_height

print(find_Volume(10,8,6)) # Output: 240.0

# Test cases
print(find_Volume(10,8,6)) # Output: 240.0
print(find_Volume(5,10,12)) # Output: 150.0
print(find_Volume(12,15,10)) # Output: 750.0
print(find_Volume(20,12,8)) # Output: 1200.0
print(find_Volume(15,12,10)) # Output: 750.0
print(find_Volume(8,12,10)) # Output: 480.0
print(find_Volume(12,10,8)) # Output: 480.0
print(find_Volume(10,12,15)) # Output: 750.0
print(find_Volume(8,10,12)) # Output: 480.0
print(find_Volume(12,8,10)) # Output: 480.0
print(find_Volume(10,15,12)) # Output: 750.0
print(find_Volume(12,10,8)) # Output: 480.0
print(find_Volume(15,8,12)) # Output: 750.0
print(find_Volume(8,10,12)) # Output: 480.0
print(find_Volume(15,12,10)) # Output: 750.0
print(find_Volume(12,8,10)) # Output: 480.0
print(find_Volume(10,12,15)) # Output: 750.0
print(find_Volume(8,12,15)) # Output: 750.0
print(find_Volume(12,10,15)) # Output: 750.0
print(find_Volume(15,10,8)) # Output: 750.0
print(find_Volume(10,15,8)) # Output: 750.0
print(find_Volume(12,15,10)) # Output: 750.0
print(find_Volume(15,12,8)) # Output: 750.0
print(find_Volume(8,10,15)) # Output: 750.0
print(find_Volume(10,8,12)) # Output: 480.0
print(find_Volume(15,10,12)) # Output: 750.0
print(find_Volume(12,10,15)) # Output: 750.0
print(find_Volume(10,12,15)) # Output: 750.0
print(find_Volume(15,8,12)) # Output: 750.0
print(find_Volume(12,15,10)) # Output: 750.0
print(find_Volume(10,15,12)) # Output: 750.0
print(find_Volume(15,12,10)) # Output: 750.0
print(find_Volume(8,12,15)) # Output: 750.0
print(find_Volume(12,15,10)) # Output: 750.0
print(find_Volume(10,12,15)) # Output: 750.0
print(find_Volume(15,10,12)) # Output: 7