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
    >>> angle_complex(1,3)
    1.3099699437565405
    >>> angle_complex(1,4)
    1.4020930067266612
    >>> angle_complex(1,5)
    1.4849057724243047
    >>> angle_complex(1,6)
    1.5257771112421087
    >>> angle_complex(1,7)
    1.5607963267948966
    >>> angle_complex(1,8)
    1.5913240501548685
    >>> angle_complex(1,9)
    1.6217943569283186
    >>> angle_complex(1,10)
    1.6519866994747318
    >>> angle_complex(1,11)
    1.6819898320262638
    >>> angle_complex(1,12)
    1.711793064577796
    >>> angle_complex(1,13)
    1.741496307129328
    >>> angle_complex(1,14)
    1.7708995506808598
    >>> angle_complex(1,15)
    1.8000000000000002
    >>> angle_complex(1,16)
    1.829102754132381
    >>> angle_complex(1,17)
    1.858005997683813
    >>> angle_complex(1,18)
    1.886709241235345
    >>> angle_complex(1,19)
    1.9152124947868779
    >>> angle_complex(1,20)
    1.9435157483384098
    >>> angle_complex(1,21)
    1.9716189918899427
    >>> angle_complex(1,22)
    2.0000000000000002
    >>> angle_complex(1,23)
    2.028312245331475
    >>> angle_complex(1,24)
    2.0564154988820078
    >>> angle_complex(1,25)
    2.0843187524326397
    >>> angle_complex(1,26)
    2.112022006083272
    >>> angle_complex(1,27)
    2.139525259633904
    >>> angle_complex(1,28)
    2.16