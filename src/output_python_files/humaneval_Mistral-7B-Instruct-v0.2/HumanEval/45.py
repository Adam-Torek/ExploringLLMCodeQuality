def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

def triangle_perimeter(a, b, c):
    """Given lengths of all sides of a triangle return perimeter.
    >>> triangle_perimeter(3, 4, 5)
    12
    """
    return a + b + c

def triangle_type(a, b, c):
    """Given lengths of sides of a triangle return type of triangle.
    >>> triangle_type(3, 4, 5)
    'Scalene'
    """
    if a == b and b == c:
        return 'Equilateral'
    elif (a == b or b == c or a == c) and (a != b or b != c or a != c):
        return 'Isosceles'
    else:
        return 'Scalene'

def main():
    """Test cases for triangle functions"""
    print(triangle_area(5, 3))
    print(triangle_perimeter(3, 4, 5))
    print(triangle_type(3, 4, 5))
    print(triangle_area(3, 3))
    print(triangle_perimeter(3, 3, 3))
    print(triangle_type(3, 3, 3))
    print(triangle_area(3, 3.5))
    print(triangle_perimeter(3, 3, 3.5))
    print(triangle_type(3, 3, 3.5))

if __name__ == '__main__':
    main()