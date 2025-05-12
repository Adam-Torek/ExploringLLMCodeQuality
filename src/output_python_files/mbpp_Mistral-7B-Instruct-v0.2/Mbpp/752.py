"""
Write a function to find the nth jacobsthal number. https://www.geeksforgeeks.org/jacobsthal-and-jacobsthal-lucas-numbers/ 0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731, ...
assert jacobsthal_num(5) == 11
"""

def jacobsthal_num(n):
    """
    :param n: int
    :return: int
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return (2 * jacobsthal_num(n // 2) + jacobsthal_num(n // 4)) % 2**(n - 1)

if __name__ == "__main__":
    for n in [0, 1, 5, 10, 15, 20]:
        print(f"jacobsthal_num({n}) = {jacobsthal_num(n)}")
    assert jacobsthal_num(5) == 11
    assert jacobsthal_num(10) == 1023
    assert jacobsthal_num(15) == 65533
    assert jacobsthal_num(20) == 1073741823
    assert jacobsthal_num(25) == 4294967293
    assert jacobsthal_num(30) == 18014398509481984
    assert jacobsthal_num(35) == 36028797018963968521
    assert jacobsthal_num(40) == 1441151880758558708811015
    assert jacobsthal_num(45) == 6345283276634696122103590621
    assert jacobsthal_num(50) == 281474976710656258210975515161615
    assert jacobsthal_num(55) == 1125899906842697636766979184014450561
    assert jacobsthal_num(60) == 46116860184273879035516161460594509417578125
    assert jacobsthal_num(65) == 184467440737095516161460594509450945094509417584105
    assert jacobsthal_num(70) == 73780539816161616606368564036856403685640368564036856403685640368564036856403685640368564036856403685640368564036856403685640368564036856403685640368564036856403685640368564036856403685640368564036856