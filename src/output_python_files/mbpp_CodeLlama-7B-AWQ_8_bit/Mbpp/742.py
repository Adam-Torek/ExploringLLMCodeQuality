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
    assert area_tetrahedron(3) == 15.588457268119894
    assert area_tetrahedron(4) == 30.866020408163265
    assert area_tetrahedron(5) == 51.13358363821663
    assert area_tetrahedron(6) == 71.401146888269905
    assert area_tetrahedron(7) == 91.66871013832316
    assert area_tetrahedron(8) == 111.93627338837642
    assert area_tetrahedron(9) == 132.20383683843069
    assert area_tetrahedron(10) == 152.47140028848496
    assert area_tetrahedron(11) == 172.73896373854023
    assert area_tetrahedron(12) == 193.0065271885945
    assert area_tetrahedron(13) == 213.27409063865077
    assert area_tetrahedron(14) == 233.54165408870704
    assert area_tetrahedron(15) == 253.80921753876331
    assert area_tetrahedron(16) == 274.07678098881968
    assert area_tetrahedron(17) == 294.34434443887605
    assert area_tetrahedron(18) == 314.61190788893233
    assert area_tetrahedron(19) == 334.88047133900061
    assert area_tetrahedron(20) == 355.1480347890679
    assert area_tetrahedron(21) == 375.4156082391342
    assert area_tetrahedron(22) == 395.6831716892015
    assert area_tetrahedron(23) == 415.9507351392688
    assert area_tetrahedron(24) == 436.2282985893361
    assert area_tetrahedron(25) == 456.5058620394034
    assert area_tetrahedron(26) == 476.7734254894697
    assert area_tetrahedron(27) == 497.04109893953705
    assert area_tetrahedron(28) == 517.3087623896043
    assert area_tetrahedron(29) == 537.5763258396716
    assert area_tetrahedron(30) == 557.84389928