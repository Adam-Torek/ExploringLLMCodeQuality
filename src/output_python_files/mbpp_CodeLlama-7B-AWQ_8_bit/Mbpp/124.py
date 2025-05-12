"""
Write a function to get the angle of a complex number.
assert math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001)
"""


def angle_complex(real, imag):
    """
    >>> angle_complex(0,1j)
    1.5707963267948966
    >>> angle_complex(1,1j)
    0.7853981633974483
    >>> angle_complex(1,0)
    0.0
    >>> angle_complex(1,1)
    0.7853981633974483
    >>> angle_complex(1,2)
    1.1071487177940904
    >>> angle_complex(1,0.5)
    0.4636476090008061
    >>> angle_complex(1,0.25)
    0.2357022509471488
    >>> angle_complex(1,0.125)
    0.11780339887695312
    >>> angle_complex(1,0.0625)
    0.05882352941176471
    >>> angle_complex(1,0.03125)
    0.034411764705882355
    >>> angle_complex(1,0.015625)
    0.017857142857142857
    >>> angle_complex(1,0.0078125)
    0.008928571428571428
    >>> angle_complex(1,0.00390625)
    0.004471428571428571
    >>> angle_complex(1,0.001953125)
    0.0022357142857142855
    >>> angle_complex(1,0.0009765625)
    0.001117647058823529
    >>> angle_complex(1,0.00048828125)
    0.000554705882352941
    >>> angle_complex(1,0.000244140625)
    0.0002723529411764706
    >>> angle_complex(1,0.0001220703125)
    0.0001361764705882353
    >>> angle_complex(1,0.00006103515625)
    0.000070078125
    >>> angle_complex(1,0.000030517578125)
    0.000035078125
    >>> angle_complex(1,0.0000152587890625)
    0.0000175390625
    >>> angle_complex(1,0.00000762939453125)
    0.00000876953125
    >>> angle_complex(1,0.000003814697265625)
    0.0000044705882352941
    >>> angle_complex(1,0.0000019073486328125)
    0.00000223