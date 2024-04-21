"""
Write a function to find the nth hexagonal number.
assert hexagonal_num(10) == 190
"""
def hexagonal_num(n):
    """
    :param n: int
    :return: int
    """
    return int(3 * (2 * n - 1) * (2 * n - 1) + 2 * (2 * n - 1))

if __name__ == "__main__":
    import unittest
    unittest.main()

    assert hexagonal_num(10) == 190
    assert hexagonal_num(1) == 1
    assert hexagonal_num(2) == 11
    assert hexagonal_num(3) == 37
    assert hexagonal_num(4) == 91
    assert hexagonal_num(5) == 171
    assert hexagonal_num(6) == 277
    assert hexagonal_num(7) == 415
    assert hexagonal_num(8) == 591
    assert hexagonal_num(9) == 792
    assert hexagonal_num(100) == 121393
    assert hexagonal_num(1000) == 15485833
    assert hexagonal_num(10000) == 196418661
    assert hexagonal_num(100000) == 24494897673
    assert hexagonal_num(1000000) == 302458837979
    assert hexagonal_num(10000000) == 3771196606311
    assert hexagonal_num(100000000) == 466968729471681
    assert hexagonal_num(1000000000) == 572204582538886721
    assert hexagonal_num(10000000000) == 69672598910561684211
    assert hexagonal_num(100000000000) == 836248008168227777673
    assert hexagonal_num(1000000000000) == 10002040816326532669761
    assert hexagonal_num(10000000000000) == 1203127110156256426982221
    assert hexagonal_num(100000000000000) == 143266966629034881695555211
    assert hexagonal_num(1000000000000000) == 1701786401680388563685288011
    assert hexagonal_num(10000000000000000) == 20155527906250041602274654441
    assert hexagonal_num(100000000000000000) == 2378147401165063262979241379201
    assert hexagonal_num(1000000000000000000) == 2802012108139400317084176634600321
    assert hexagonal_num(10000000000000000000) == 33003293321110953088377