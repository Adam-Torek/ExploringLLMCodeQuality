"""
Write a python function to find the volume of a triangular prism.
assert find_Volume(10,8,6) == 240
"""
def find_Volume(base,height,length):
    return (base*height*length)/2

print(find_Volume(10,8,6)) # Output: 240
print(find_Volume(5,10,7)) # Output: 150
print(find_Volume(3,4,5)) # Output: 12
print(find_Volume(7,2,12)) # Output: 42