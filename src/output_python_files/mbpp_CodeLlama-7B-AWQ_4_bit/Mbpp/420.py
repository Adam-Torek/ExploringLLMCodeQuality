"""
Write a python function to find the cube sum of first n even natural numbers.
assert cube_Sum(2) == 72
"""


def cube_Sum(n):
    """
    >>> cube_Sum(2)
    72
    >>> cube_Sum(3)
    1728
    >>> cube_Sum(4)
    3744
    >>> cube_Sum(5)
    6760
    >>> cube_Sum(6)
    10864
    >>> cube_Sum(7)
    16000
    >>> cube_Sum(8)
    26400
    >>> cube_Sum(9)
    39600
    >>> cube_Sum(10)
    60640
    >>> cube_Sum(11)
    81840
    >>> cube_Sum(12)
    114000
    >>> cube_Sum(13)
    150240
    >>> cube_Sum(14)
    195040
    >>> cube_Sum(15)
    248320
    >>> cube_Sum(16)
    308640
    >>> cube_Sum(17)
    378960
    >>> cube_Sum(18)
    459280
    >>> cube_Sum(19)
    559600
    >>> cube_Sum(20)
    669920
    >>> cube_Sum(21)
    790240
    >>> cube_Sum(22)
    930560
    >>> cube_Sum(23)
    1080880
    >>> cube_Sum(24)
    1241200
    >>> cube_Sum(25)
    1411520
    >>> cube_Sum(26)
    1581840
    >>> cube_Sum(27)
    1762160
    >>> cube_Sum(28)
    1942480
    >>> cube_Sum(29)
    2132800
    >>> cube_Sum(30)
    2333120
    >>> cube_Sum(31)
    2533440
    >>> cube_Sum(32)
    2733760
    >>> cube_Sum(33)
    2934080
    >>> cube_Sum(34)
    3134400
    >>> cube_Sum(35)
    3334720
    >>> cube_Sum(36)
    3535040
    >>> cube_Sum(37)
    3735360
    >>> cube_Sum(38)
    3935680
    >>> cube_Sum(39)
    4136000
    >>> cube_Sum(40)
    4336320
    >>> cube_Sum(41)
    4536640
    >>> cube_Sum(42)
    4736960
    >>> cube_Sum(43)
    4937280
    >>> cube_Sum(44)
    5137600
    >>> cube_Sum(45)
    5337920
    >>> cube_Sum(46)
    5538240
    >>> cube_Sum(47)
    5738560
    >>> cube_Sum(48)
    5938880
    >>> cube_Sum(49)
    6139200
    >>> cube_Sum(50)
    6339520
    >>> cube_Sum(51)
    6539840
    >>> cube_Sum(52)
    6740160
    >>> cube_Sum(53)
    6940480
    >>> cube_Sum(54)
    714