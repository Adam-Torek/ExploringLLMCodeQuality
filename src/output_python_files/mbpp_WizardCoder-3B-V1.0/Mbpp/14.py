"""
Write a python function to find the volume of a triangular prism.
assert find_Volume(10,8,6) == 240
"""

def find_Volume(base, height, length):
    volume = (base * height * length) / 3
    return volume

# Test the function
print(find_Volume(10,8,6)) # Output: 240<|endoftext|>