from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join(chr(int(x, 2) ^ int(y, 2)) for x, y in zip(a, b))


def string_xor_all(strings: List[str]) -> str:
    """ Input is a list of strings a, b, ..., n consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor_all(['010', '110', '101'])
    '111'
    """
    return ''.join(chr(int(x, 2) ^ int(y, 2)) for x, y in zip(*strings))