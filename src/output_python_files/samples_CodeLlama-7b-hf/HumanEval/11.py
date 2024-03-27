from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return "".join(map(lambda x, y: str(int(x) ^ int(y)), a, b))


def string_xor_list(a: List[str], b: List[str]) -> List[str]:
    """ Input are two lists of strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of strings.
    >>> string_xor_list(['010', '110'], ['101', '011'])
    ['111', '100']
    """
    return [string_xor(a[i], b[i]) for i in range(len(a))]


def string_xor_matrix(a: List[List[str]], b: List[List[str]]) -> List[List[str]]:
    """ Input are two lists of lists of strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of lists of strings.
    >>> string_xor_matrix([['010', '110'], ['101', '011']], [['100', '110'], ['101', '011']])
    [['111', '100'], ['101', '010']]
    """
    return [string_xor_list(a[i], b[i]) for i in range(len(a))]


def string_xor_matrix_2d(a: List[List[str]], b: List[List[str]]) -> List[List[str]]:
    """ Input are two lists of lists of strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of lists of strings.
    >>> string_xor_matrix_2d([['010', '110'], ['101', '011']], [['100', '110'], ['101', '011']])
    [['111', '100'], ['101', '010']]
    """
    return [string_xor_list(a[i], b[i]) for i in range(len(a))]


def string_xor_matrix_3d(a: List[List[List[str]]], b: List[List[List[str]]]) -> List[List[List[str]]]:
    """ Input are two lists of lists of lists of strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of lists of lists of strings.
    >>> string_xor_matrix_3d([[['010', '110'], ['101', '011']], [['100', '110'], ['101', '011']]], [[['100', '110'], ['101', '011']], [['100', '110'], ['101', '011']]])
    [[['111', '100'], ['101', '010']], [['111', '100'], ['101', '010']]]
    """
    return [string_xor_matrix(a[i], b[i]) for i in range(len(a))]


def string_xor_matrix_4d(a: List[List[List[List[str]]]], b: List[List[List[List[str]]]]) -> List[List[List[List[str]]]]:
    """ Input are two lists of lists of lists of lists of strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of lists of lists of lists of strings.