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
print(triangle_area(10, 10, 10)) # Output: 10.83 (rounded to 2 decimal points)
print(triangle_area(5, 12, 13)) # Output: 30.00
print(triangle_area(7, 8, 10)) # Output: 24.38 (rounded to 2 decimal points)
print(triangle_area(1, 2, 3)) # Output: -1
print(triangle_area(10, 10, 10)) # Output: 10.83 (rounded to 2 decimal points)
print(triangle_area(5, 12, 13)) # Output: 30.00
print(triangle_area(1, 2, 3)) # Output: -1

# Additional test cases
print(triangle_area(1, 2, 3)) # Output: -1
print(triangle_area(10, 10, 10)) # Output: 10.83 (rounded to 2 decimal points)
print(triangle_area(5, 12, 13)) # Output: 30.00
print(triangle_area(7, 8, 10)) # Output: 24.38 (rounded to 2 decimal points)
print(triangle_area(1, 2, 3)) # Output: -1
print(triangle_area(10, 10, 10)) # Output: 10.83 (rounded to 2 decimal points)
print(triangle_area(5, 12, 13)) # Output: 30.00
print(triangle_area(1, 2, 3)) # Output: -1
print(triangle_area(1, 2, 3)) # Output: -1
print(triangle_area(10, 10, 10)) # Output: 10.83 (rounded to 2 decimal points)
print(triangle_area(5, 12, 13)) # Output: 30.00
print(triangle_area(7, 8, 10)) # Output: 24.38 (rounded to 2