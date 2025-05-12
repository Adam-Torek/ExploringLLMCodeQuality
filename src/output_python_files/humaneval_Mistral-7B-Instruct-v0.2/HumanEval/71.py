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
    if a + b > c and b + c > a and a + c > b:
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return round(area, 2)
    else:
        return -1

# Test cases
print(triangle_area(3, 4, 5))
print(triangle_area(1, 2, 10))
print(triangle_area(5, 12, 13))
print(triangle_area(3, 3, 3))
print(triangle_area(3, 3, 6))