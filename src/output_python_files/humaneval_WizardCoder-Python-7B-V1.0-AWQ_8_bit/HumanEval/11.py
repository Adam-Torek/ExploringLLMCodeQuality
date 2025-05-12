from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join(['1' if a[i] != b[i] else '0' for i in range(len(a))])

def string_xor_list(a: List[str], b: List[str]) -> List[str]:
    """ Input are two lists of strings a and b, each consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result as a list of strings.
    >>> string_xor_list(['010', '110'], ['101', '111'])
    ['101', '001']
    """
    return [string_xor(a[i], b[i]) for i in range(len(a))]

if __name__ == "__main__":
    import doctest
    doctest.testmod()