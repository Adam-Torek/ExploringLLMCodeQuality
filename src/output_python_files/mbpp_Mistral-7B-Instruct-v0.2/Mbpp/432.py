"""
Write a function to find the median length of a trapezium.
assert median_trapezium(15,25,35)==20
"""
def median_trapezium(a, b, c):
    # Calculate the area of the trapezium using the formula: area = (a + b) * h / 2
    h = (2 * area(a, b, c)) / (a + b)
    # The median is the height, so just return it
    return h

def area(a, b, c):
    # The area of a trapezium is given by the formula: area = (a + b) * h / 2
    return ((a + b) * c) / 2

assert median_trapezium(15, 25, 35) == 20</s>