"""
Write a function to find the perimeter of a regular pentagon from the length of its sides.
assert perimeter_pentagon(5) == 25
"""

def perimeter_pentagon(side_length):
    return 5 * side_length

print(perimeter_pentagon(5)) # Output: 25
print(perimeter_pentagon(10)) # Output: 50
print(perimeter_pentagon(1) == 5) # Output: False
print(perimeter_pentagon(10) == 50) # Output: False

# Test cases
assert perimeter_pentagon(5) == 25
assert perimeter_pentagon(10) == 50
assert perimeter_pentagon(1) != 5
assert perimeter_pentagon(10) != 50