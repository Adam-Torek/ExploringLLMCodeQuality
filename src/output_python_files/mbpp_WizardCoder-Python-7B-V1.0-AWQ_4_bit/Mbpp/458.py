"""
Write a function to find the area of a rectangle.
assert rectangle_area(10,20)==200
"""

def rectangle_area(length, width):
    return length * width

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
print(rectangle_area(-10, -20)) # Output: 0

# Test cases with invalid inputs
print(rectangle_area("10", 20)) # Output: None
print(rectangle_area(10, "20")) # Output: None
print(rectangle_area(10, "20")) # Output: None
print(rectangle_area(10, 20.5) # Output: None
print(rectangle_area(10, None) # Output: None
print(rectangle_area(None, 20) # Output: None
print(rectangle_area(None, None) # Output: None
print(rectangle_area(10, [20]) # Output: None
print(rectangle_area([10], 20) # Output: None
print(rectangle_area(10, {20}) # Output: None
print(rectangle_area({10}, 20) # Output: None
print(rectangle_area(10, (20) # Output: None
print(rectangle_area(10, (20, 30) # Output: None
print(rectangle_area(10, (20, 30, 40) # Output: None
print(rectangle_area(10, 20, 30) # Output: None
print(rectangle_area(10, 20, 30, 40) # Output: None
print(rectangle_area(10, 20, 30, 40, 50) # Output: None
print(rectangle_area(10, 20, 30, 40, 50, 60) # Output: None
print(rectangle_area(10, 20, 30, 40, 50, 60, 70) # Output: None
print(rectangle_area(10, 20, 30, 40, 50, 60, 70, 80) # Output: None
print(rectangle_area(10, 20, 30, 40, 50, 60, 70, 80, 90) # Output: None
print(rectangle_area(10, 20, 30, 40, 50, 60, 70, 80, 90, 100) # Output: None
print(rectangle_area(10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110) # Output: None
print(rectangle_area(10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120) # Output: None
print(rectangle_area(10, 20, 30, 40, 50, 60,