"""
Write a function to find the nth nonagonal number.
assert is_nonagonal(10) == 325
"""

def is_nonagonal(n):
    """
    Check if a number is nonagonal
    """
    if n % 3 == 0:
        return False
    if n % 5 == 0:
        return False
    if n % 15 == 0:
        return False
    if n % 20 == 0:
        return False
    if n % 60 == 0:
        return False
    return True

def nth_nonagonal_number(n):
    """
    Find the nth nonagonal number
    """
    if n % 3 == 0:
        return (n // 3) * (2 * 3 + 1)
    if n % 5 == 0:
        return (n // 5) * (2 * 5 + 1)
    if n % 15 == 0:
        return (n // 15) * (2 * 15 + 1)
    if n % 20 == 0:
        return (n // 20) * (2 * 20 + 1)
    if n % 60 == 0:
        return (n // 60) * (2 * 60 + 1)
    raise ValueError("n must be a multiple of 3, 5, 15, 20 or 60")


if __name__ == '__main__':
    assert is_nonagonal(10) == True
    assert nth_nonagonal_number(10) == 325
    assert nth_nonagonal_number(15) == 1005
    assert nth_nonagonal_number(20) == 2000
    assert nth_nonagonal_number(25) == 2500
    assert nth_nonagonal_number(30) == 3000
    assert nth_nonagonal_number(35) == 3500
    assert nth_nonagonal_number(40) == 4000
    assert nth_nonagonal_number(45) == 4500
    assert nth_nonagonal_number(50) == 5000
    assert nth_nonagonal_number(55) == 5500
    assert nth_nonagonal_number(60) == 6000
    assert nth_nonagonal_number(65) == 6500
    assert nth_nonagonal_number(70) == 7000
    assert nth_nonagonal_number(75) == 7500
    assert nth_nonagonal_number(80) == 8000
    assert nth_nonagonal_number(85) == 8500
    assert nth_nonagonal_number(90) == 9000
    assert nth_nonagonal_number(95) == 9500
    assert nth_nonagonal_number(100) == 10000
    assert nth_nonagonal_number(105) == 10500
    assert nth_nonagonal_number(110) == 11000
    assert nth_nonagonal_number(115) == 11500
    assert nth_nonagonal_number(120) == 12000
    assert nth_nonagonal_number(125) == 12500
    assert nth_nonagonal_number(130) == 13000
    assert nth_nonagonal_number(135) == 13500
    assert nth_nonagonal_number(140) == 14000
    assert nth_nonagonal_number(145) == 14500
    assert nth_nonagonal_number(150) == 15000
    assert nth_nonagonal_number(155) == 15500
    assert nth_nonagonal_number(160) == 160