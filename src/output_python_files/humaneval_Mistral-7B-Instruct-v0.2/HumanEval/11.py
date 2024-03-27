from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join(map(lambda x, y: str(int(x) ^ int(y)), a, b))


def find_single_bit_flip(s: str, t: str) -> str:
    """ Given two strings s and t of equal length, find the string that
    differs from s by exactly one bit.
    >>> find_single_bit_flip('01101101', '01101100')
    '01101100'
    """
    xor_result = string_xor(s, t)
    for i in range(len(xor_result)):
        if xor_result[i] == '1':
            flip_string = s[:i] + '0' + s[i+1:]
            return flip_string


def find_two_strings_with_only_one_bit_difference(strings: List[str]) -> List[List[str]]:
    """ Given a list of strings, find pairs of strings that differ by exactly one bit.
    >>> find_two_strings_with_only_one_bit_difference(['01101101', '01101100', '11110101'])
    [['01101101', '01101100'], ['01101101', '11110101']]
    """
    result = []
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) == len(strings[j]):
                if len(string_xor(strings[i], strings[j])) == 1:
                    result.append([strings[i], strings[j]])
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print(find_two_strings_with_only_one_bit_difference(['01101101', '01101100', '11110101']))
    print(find_two_strings_with_only_one_bit_difference(['11111111', '01111110', '10111110']))
    print(find_two_strings_with_only_one_bit_difference(['11111111', '11111111']))</s>