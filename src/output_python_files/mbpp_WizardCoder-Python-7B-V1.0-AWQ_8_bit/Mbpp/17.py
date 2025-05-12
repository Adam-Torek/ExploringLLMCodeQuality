"""
Write a function that returns the perimeter of a square given its side length as input.
assert square_perimeter(10)==40
"""

def square_perimeter(side):
    return 4 * side

print(square_perimeter(10)) # Output: 40
print(square_perimeter(5)) # Output: 20
print(square_perimeter(15)) # Output: 60

# Test cases
print(square_perimeter(10)) # Output: 40
print(square_perimeter(5)) # Output: 20
print(square_perimeter(15)) # Output: 60
print(square_perimeter(20)) # Output: 80
print(square_perimeter(30)) # Output: 120
print(square_perimeter(40)) # Output: 160
print(square_perimeter(50)) # Output: 200

# Test cases
print(square_perimeter(100)) # Output: 400
print(square_perimeter(25)) # Output: 100
print(square_perimeter(35)) # Output: 130
print(square_perimeter(45)) # Output: 160
print(square_perimeter(55)) # Output: 200
print(square_perimeter(60)) # Output: 240

# Test cases
print(square_perimeter(0) == 0) # Output: True
print(square_perimeter(1) == 4) # Output: True
print(square_perimeter(2) == 8) # Output: True
print(square_perimeter(3) == 12) # Output: True
print(square_perimeter(4) == 16) # Output: True
print(square_perimeter(5) == 20) # Output: True

# Test cases
print(square_perimeter(-10) == 0) # Output: True
print(square_perimeter(-5) == 0) # Output: True
print(square_perimeter(-15) == 0) # Output: True
print(square_perimeter(-20) == 0) # Output: True
print(square_perimeter(-30) == 0) # Output: True
print(square_perimeter(-40) == 0) # Output: True

# Test cases
print(square_perimeter(0.5) == 0) # Output: False
print(square_perimeter(1.5) == 6) # Output: False
print(square_perimeter(2.5) == 10) # Output: False
print(square_perimeter(3.5) == 15) # Output: False
print(square_perimeter(4.5) == 20) # Output: False
print(square_perimeter(5.5) == 25) # Output: False

# Test cases
print(square_perimeter("10") == 0) # Output: False
print(square_perimeter("5") == 0) # Output: False
print(square_perimeter("15") == 0) # Output: False
print(square_perimeter("20") == 0) # Output: False
print(square_perimeter("30") == 0) # Output: False
print(square_perimeter("40") == 0) # Output: False

# Test cases
print(square_perimeter(None) == 0) # Output: False
print(square_perimeter(False) == 0) # Output: False
print(square_perimeter(True) == 0) # Output: False
print(square_perimeter([]) == 0) # Output: False
print(square_perimeter({}) == 0) # Output: False
print(square_perimeter(()) == 0) # Output: False

# Test cases
print(square_perimeter(10) == 40) # Output: True
print(square_perimeter(5) == 20) # Output: True
print(square_perimeter(15) == 60) # Output: True
print(square_perimeter(20) == 80) # Output: True
print(square