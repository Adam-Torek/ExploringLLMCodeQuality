"""
Write a function to find the area of a rectangle.
assert rectangle_area(10,20)==200
"""
def rectangle_area(width, height):
    """
    This function calculates the area of a rectangle.
    :param width: the width of the rectangle
    :param height: the height of the rectangle
    :return: the area of the rectangle
    """
    area = width * height
    return area

#test the function
assert rectangle_area(10,20)==200