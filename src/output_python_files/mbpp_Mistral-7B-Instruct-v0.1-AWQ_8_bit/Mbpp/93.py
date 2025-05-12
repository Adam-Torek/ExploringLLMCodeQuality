"""
Write a function to calculate the value of 'a' to the power 'b'.
assert power(3,4) == 81
"""

def power(a, b):
    """
    Calculate the value of 'a' to the power 'b'
    """
    result = a
    for i in range(1, b):
        result *= a
    return result

# assert power(3,4) == 81
# assert power(2,5) == 32
# assert power(1,6) == 1
# assert power(0,7) == 0
# assert power(-1,7) == -127
# assert power(-2,7) == -256
# assert power(-3,7) == -387
# assert power(-4,7) == -518
# assert power(-5,7) == -650
# assert power(-6,7) == -782
# assert power(-7,7) == -914
# assert power(-8,7) == -1046
# assert power(-9,7) == -1178
# assert power(-10,7) == -1310
# assert power(-11,7) == -1442
# assert power(-12,7) == -1574
# assert power(-13,7) == -1706
# assert power(-14,7) == -1838
# assert power(-15,7) == -2070
# assert power(-16,7) == -2302
# assert power(-17,7) == -2534
# assert power(-18,7) == -2766
# assert power(-19,7) == -3000
# assert power(-20,7) == -3234
# assert power(-21,7) == -3468
# assert power(-22,7) == -3702
# assert power(-23,7) == -3936
# assert power(-24,7) == -4170
# assert power(-25,7) == -4394
# assert power(-26,7) == -4618
# assert power(-27,7) == -4842
# assert power(-28,7) == -5066
# assert power(-29,7) == -5290
# assert power(-30,7) == -5514
# assert power(-31,7) == -5738
# assert power(-32,7) == -6062
# assert power(-33,7) == -6386
# assert power(-34,7) == -6710
# assert power(-35,7) == -7034
# assert power(-36,7) == -7358
# assert power(-37,7) == -7682
# assert power(-38,7) == -8006
# assert power(-39,7) == -8330
# assert power(-40,7) == -8654
# assert power(-41,7) == -9078
# assert power(-42,7) == -9502
# assert power(-43,7) == -10026
# assert power(-44,7) == -10550
# assert power(-45,7) == -11074
# assert power(-46,7) == -11608
# assert power(-47,7) == -12142
# assert power(-48,7) == -12676
# assert power(-49,7) == -13210
# assert power(-50,7) == -13744
# assert power(-51,7) == -14278
# assert power(-52,7) == -14812
# assert power(-53,7) == -15346
# assert power(-54,7) == -15880
# assert power(-55,7) == -16414
# assert power(-5