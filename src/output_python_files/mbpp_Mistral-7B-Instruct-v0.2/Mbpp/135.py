"""
Write a function to find the nth hexagonal number.
assert hexagonal_num(10) == 190
"""
def hexagonal_num(n):
    """
    :param n: int, the nth hexagonal number to find
    :return: int, the nth hexagonal number
    """
    return int(3 * (n * (n + 1)) / 2)

if __name__ == "__main__":
    import unittest
    unittest.main()

    assert hexagonal_num(10) == 190
    assert hexagonal_num(1) == 1
    assert hexagonal_num(2) == 7
    assert hexagonal_num(3) == 19
    assert hexagonal_num(4) == 43
    assert hexagonal_num(5) == 81
    assert hexagonal_num(6) == 135
    assert hexagonal_num(7) == 207
    assert hexagonal_num(8) == 299
    assert hexagonal_num(9) == 421
    assert hexagonal_num(100) == 112137
    assert hexagonal_num(1000) == 330550131
    assert hexagonal_num(10000) == 10314312211
    assert hexagonal_num(100000) == 3350580781611
    assert hexagonal_num(1000000) == 1059218608292211
    assert hexagonal_num(10000000) == 341645462290670711
    assert hexagonal_num(100000000) == 109461688053144706811
    assert hexagonal_num(1000000000) == 35338605329832716049611
    assert hexagonal_num(10000000000) == 11132924810975586679234311
    assert hexagonal_num(100000000000) == 362265661584772879091895351611
    assert hexagonal_num(1000000000000) == 1176690304602486555921296393601
    assert hexagonal_num(10000000000000) == 3836394305195135923738267293604911
    assert hexagonal_num(100000000000000) == 12378154905718713378043612608166061
    assert hexagonal_num(1000000000000000) == 409600016395348612204888923791464449
    assert hexagonal_num(10000000000000000) == 1316166467771377358185268123518960512003
    assert hexagonal_num(100000000000000000) == 436