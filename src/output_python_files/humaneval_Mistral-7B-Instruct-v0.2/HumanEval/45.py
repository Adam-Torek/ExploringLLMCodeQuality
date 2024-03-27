def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

def triangle_perimeter(a, b, c):
    """Given lengths of sides a, b, c return perimeter for a triangle.
    >>> triangle_perimeter(3, 4, 5)
    12.0
    """
    return a + b + c

def triangle_is_valid(a, b, c):
    """Given lengths of sides a, b, c return True if triangle is valid, False otherwise.
    >>> triangle_is_valid(3, 4, 5)
    True
    """
    return a + b > c and a + c > b and b + c > a

def main():
    """Test triangle functions"""
    print(triangle_area(5, 3))
    print(triangle_perimeter(3, 4, 5))
    print(triangle_is_valid(3, 4, 5))
    print(triangle_is_valid(3, 3, 3))
    print(triangle_is_valid(3, 3, 4))

if __name__ == '__main__':
    main()</s>