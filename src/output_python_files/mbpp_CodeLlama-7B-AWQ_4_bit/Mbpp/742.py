"""
Write a function to caluclate the area of a tetrahedron.
assert area_tetrahedron(3)==15.588457268119894
"""


def area_tetrahedron(a):
    """
    a: float

    returns: float
    """
    return (a**2 * (sqrt(2 * (3 * a ** 2 - a ** 4)))) / 12


def test_area_tetrahedron():
    """
    Tests area_tetrahedron
    """
    assert area_tetrahedron(3) == 15.588457268119894


def main():
    """
    Runs area_tetrahedron
    """
    print(area_tetrahedron(3))


if __name__ == "__main__":
    main()