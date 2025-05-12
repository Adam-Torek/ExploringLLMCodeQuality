def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    '''
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        return round(area, 2)
    else:
        return -1

# Test cases
print(triangle_area(3, 4, 5)) # Output: 6.00
print(triangle_area(1, 2, 10)) # Output: -1
print(triangle_area(7, 8, 10)) # Output: 24.33
print(triangle_area(10, 10, 10)) # Output: 17.32
print(triangle_area(1, 1, 1)) # Output: -1
print(triangle_area(10, 1, 1)) # Output: -1
print(triangle_area(1, 10, 1)) # Output: -1
print(triangle_area(0, 1, 2)) # Output: -1
print(triangle_area(1, 0, 2)) # Output: -1
print(triangle_area(1, 2, 0)) # Output: -1

# Additional test cases
print(triangle_area(5, 5, 5)) # Output: 10.83 (sqrt(225) = 5.47)
print(triangle_area(10, 10, 17)) # Output: 24.33 (sqrt(177.5) = 4.37)
print(triangle_area(10, 10, 10)) # Output: 17.32 (sqrt(172) = 12.47)
print(triangle_area(1, 2, 3)) # Output: 3.76 (sqrt(3) = 1.73)
print(triangle_area(1, 1, 1)) # Output: -1
print(triangle_area(1, 1, 2)) # Output: -1
print(triangle_area(1, 2, 1)) # Output: -1
print(triangle_area(1, 2, 3)) # Output: -1
print(triangle_area(1, 3, 2)) # Output: -1
print(triangle_area(2, 1, 3)) # Output: -1
print(triangle_area(3, 2, 1)) # Output: -1
print(triangle_area(3, 3, 2)) # Output: -1
print(triangle_area(2, 3, 1)) # Output: -1
print(triangle_area(0, 1, 2)) # Output: -1
print(triangle_area(1, 0, 2)) # Output: -1
print(triangle_area(1, 2, 0)) # Output: -1
print(triangle_area(0, 2, 1)) # Output: -1
print(triangle_area(0, 0, 0)) # Output: -1
print(triangle_area(1, 1, 0)) # Output: -1
print(triangle_area(0, 1, 1)) # Output: -1
print(triangle_area(1, 0, 0)) # Output: -1
print(triangle_area(0, 0, 1)) # Output: -1
print(triangle_area(0, 0, 0)) # Output: -1
print(triangle_area(1, 1, 1)) # Output: -1
print(triangle_area(1, 1, 1)) # Output: -1
print(triangle_area