"""
Write a function to find the third side of a right angled triangle.
assert otherside_rightangle(7,8)==10.63014581273465
"""


def otherside_rightangle(a, b):
    """
    a, b: positive integers
    returns: float, the length of the third side of the right angled triangle
    """
    # Your code here
    return (a**2 + b**2)**0.5


def test_otherside_rightangle():
    """
    Tests for otherside_rightangle
    """
    assert otherside_rightangle(7, 8) == 10.63014581273465
    assert otherside_rightangle(1, 1) == 1.7320508075688772
    assert otherside_rightangle(1, 2) == 2.23606797749979
    assert otherside_rightangle(1, 3) == 2.449489742783178
    assert otherside_rightangle(1, 4) == 2.6457513110645907
    assert otherside_rightangle(1, 5) == 2.8284271247461903
    assert otherside_rightangle(1, 6) == 3.0000000000000004
    assert otherside_rightangle(1, 7) == 3.1622776601683795
    assert otherside_rightangle(1, 8) == 3.316624790355399
    assert otherside_rightangle(1, 9) == 3.4641016151377544
    assert otherside_rightangle(1, 10) == 3.605551275463989
    assert otherside_rightangle(1, 11) == 3.744028189281224
    assert otherside_rightangle(1, 12) == 3.879428712268046
    assert otherside_rightangle(1, 13) == 4.011929235254865
    assert otherside_rightangle(1, 14) == 4.142429758242684
    assert otherside_rightangle(1, 15) == 4.269920271230503
    assert otherside_rightangle(1, 16) == 4.395410784218322
    assert otherside_rightangle(1, 17) == 4.520901297196141
    assert otherside_rightangle(1, 18) == 4.64549171017406
    assert otherside_rightangle(1, 19) == 4.768982223151979
    assert otherside_rightangle(1, 20) == 4.891472736129898
    assert otherside_rightangle(1, 21) == 5.012963250107817
    assert otherside_rightangle(1, 22) == 5.134453763085736
    assert otherside_rightangle(1, 23) == 5.254944276063655
    assert otherside_rightangle(1, 24) == 5.374434789041574
    assert otherside_rightangle(1, 25) == 5.4929252020204