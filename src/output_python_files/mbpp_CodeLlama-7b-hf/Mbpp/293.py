"""
Write a function to find the third side of a right angled triangle.
assert otherside_rightangle(7,8)==10.63014581273465
"""


def otherside_rightangle(a, b):
    """
    a, b: positive integers
    returns: the length of the third side of the right angled triangle
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
    assert otherside_rightangle(1, 12) == 3.880700123011347
    assert otherside_rightangle(1, 13) == 4.015459046839571
    assert otherside_rightangle(1, 14) == 4.150117970667794
    assert otherside_rightangle(1, 15) == 4.283776893495923
    assert otherside_rightangle(1, 16) == 4.416335816324056
    assert otherside_rightangle(1, 17) == 4.548894739152289
    assert otherside_rightangle(1, 18) == 4.681453662080423
    assert otherside_rightangle(1, 19) == 4.813912584908656
    assert otherside_rightangle(1, 20) == 4.946371507736889
    assert otherside_rightangle(1, 21) == 5.078830430565122
    assert otherside_rightangle(1, 22) == 5.211289353393355
    assert otherside_rightangle(1, 23) == 5.343748276221588
    assert otherside_rightangle(1, 24) == 5.476107199049821
    assert otherside_