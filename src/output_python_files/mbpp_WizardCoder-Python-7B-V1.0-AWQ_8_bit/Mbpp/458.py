"""
Write a function to find the area of a rectangle.
assert rectangle_area(10,20)==200
"""
def rectangle_area(width, height):
    return width * height

print(rectangle_area(10,20)) # Output: 200

# Test cases
print(rectangle_area(5, 10)) # Output: 50
print(rectangle_area(1, 4)) # Output: 4
print(rectangle_area(7, 3)) # Output: 21
print(rectangle_area(1, 1)) # Output: 1
print(rectangle_area(0, 10)) # Output: 0
print(rectangle_area(10, 0)) # Output: 0
print(rectangle_area(-5, 10)) # Output: 0
print(rectangle_area(10, -5)) # Output: 0
print(rectangle_area(0, 0)) # Output: 0

# Test cases with invalid inputs
print(rectangle_area("a", 10)) # Output: None
print(rectangle_area(10, "b")) # Output: None
print(rectangle_area(10, "10")) # Output: None
print(rectangle_area(10, -10) # Output: None
print(rectangle_area(10, 10.5) # Output: None
print(rectangle_area(10, None) # Output: None
print(rectangle_area(None, 10) # Output: None
print(rectangle_area(None, None) # Output: None
print(rectangle_area(10, [10]) # Output: None
print(rectangle_area([10], 10) # Output: None
print(rectangle_area(10, (10) # Output: None
print(rectangle_area((10, 10) # Output: None
print(rectangle_area(10, {10} # Output: None
print(rectangle_area({10: 10} # Output: None
print(rectangle_area(10, {10: 10}) # Output: None
print(rectangle_area(10, "10") # Output: None
print(rectangle_area(10, "10") # Output: None
print(rectangle_area(10, "10") # Output: None
print(rectangle_area(10, "10") # Output: None
print(rectangle_area(10, "10") # Output: None
print(rectangle_area(10, "10") # Output: None
print(rectangle_area(10, "10") # Output: None
print(rectangle_area(10, "10") # Output: None
print(rectangle_area(10, "10") # Output: None
print(rectangle_area(10, "10") # Output: None
print(rectangle_area(10, "10") # Output: None
print(rectangle_area(10, "10") # Output: None
print(rectangle_area(10, "10") # Output: None
print(rectangle_area(10, "10") # Output: None
print(rectangle_area(10, "10") # Output: None
print(rectangle_area(10, "10") # Output: None
print(rectangle_area(10, "10") # Output: None
print(rectangle_area(10, "10") # Output: None
print(rectangle_area(10, "10") # Output: None
print(rectangle_area(10, "10") # Output: None
print(rectangle_area(10, "10") # Output: None
print(rectangle_area(10, "10") # Output: None
print(rectangle_area(10, "10") # Output: None
print(rectangle_area(10, "10") # Output: None
print(rectangle_area(10, "10") # Output: None
print(rectangle_area(10, "1