"""
Write a function to find the median length of a trapezium.
assert median_trapezium(15,25,35)==20
"""


def median_trapezium(a, b, c):
    """
    :param a:
    :param b:
    :param c:
    :return:
    """
    return (a + b + c) / 2


if __name__ == '__main__':
    print(median_trapezium(15, 25, 35))
    print(median_trapezium(10, 20, 30))
    print(median_trapezium(10, 20, 30, 40))
    print(median_trapezium(10, 20, 30, 40, 50))
    print(median_trapezium(10, 20, 30, 40, 50, 60))
    print(median_trapezium(10, 20, 30, 40, 50, 60, 70))
    print(median_trapezium(10, 20, 30, 40, 50, 60, 70, 80))
    print(median_trapezium(10, 20, 30, 40, 50, 60, 70, 80, 90))
    print(median_trapezium(10, 20, 30, 40, 50, 60, 70, 80, 90, 100))
    print(median_trapezium(10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110))
    print(median_trapezium(10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120))
    print(median_trapezium(10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130))
    print(median_trapezium(10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140))
    print(median_trapezium(10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150))
    print(median_trapezium(10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160))
    print(median_trapezium(10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170))
    print(median_trapezium(10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150,