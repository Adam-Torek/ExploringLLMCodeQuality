"""
Write a function to determine if the sum of the divisors of two integers are the same.
assert are_equivalent(36, 57) == False
"""


def are_equivalent(a, b):
    """
    Write a function to determine if the sum of the divisors of two integers are the same.
    assert are_equivalent(36, 57) == False
    """
    if a == b:
        return True
    if a < b:
        a, b = b, a
    if a % 2 == 0:
        if b % 2 == 0:
            return are_equivalent(a / 2, b / 2)
        else:
            return are_equivalent(a / 2, b)
    else:
        if b % 2 == 0:
            return are_equivalent(a, b / 2)
        else:
            return are_equivalent(a, b - 1)


def test_are_equivalent():
    assert are_equivalent(36, 57) == False
    assert are_equivalent(36, 54) == True
    assert are_equivalent(36, 55) == False
    assert are_equivalent(36, 56) == False
    assert are_equivalent(36, 57) == False
    assert are_equivalent(36, 58) == False
    assert are_equivalent(36, 59) == False
    assert are_equivalent(36, 60) == False
    assert are_equivalent(36, 61) == False
    assert are_equivalent(36, 62) == False
    assert are_equivalent(36, 63) == False
    assert are_equivalent(36, 64) == False
    assert are_equivalent(36, 65) == False
    assert are_equivalent(36, 66) == False
    assert are_equivalent(36, 67) == False
    assert are_equivalent(36, 68) == False
    assert are_equivalent(36, 69) == False
    assert are_equivalent(36, 70) == False
    assert are_equivalent(36, 71) == False
    assert are_equivalent(36, 72) == False
    assert are_equivalent(36, 73) == False
    assert are_equivalent(36, 74) == False
    assert are_equivalent(36, 75) == False
    assert are_equivalent(36, 76) == False
    assert are_equivalent(36, 77) == False
    assert are_equivalent(36, 78) == False
    assert are_equivalent(36, 79) == False
    assert are_equivalent(36, 80) == False
    assert are_equivalent(36, 81) == False
    assert are_equivalent(36, 82) == False
    assert are_equivalent(36, 83) == False
    assert are_equivalent(36, 84) == False
    assert are_equivalent(36, 85) == False
    assert are_equivalent(36, 86) == False
    assert are_equivalent(36, 87) == False
    assert are_equivalent(36, 88) == False
    assert are_equivalent(36, 89) == False
    assert are_equivalent(36, 90) == False
    assert are_equivalent(36, 91) == False
    assert are_equivalent(36, 92) == False
    assert are_equivalent(36, 93) == False
    assert are_equivalent(36, 94) == False
    assert are_equivalent(36, 95) == False
    assert are_equivalent(36, 96) == False
    assert are_equivalent(36, 97) == False
    assert are_equivalent(36, 98)