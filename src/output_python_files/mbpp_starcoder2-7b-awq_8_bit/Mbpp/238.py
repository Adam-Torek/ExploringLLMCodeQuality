"""
Write a python function to count the number of non-empty substrings of a given string.
assert number_of_substrings("abc") == 6
"""

def number_of_substrings(string):
    """
    :param string: string
    :return: number of non-empty substrings
    """
    return len(set(string))


if __name__ == '__main__':
    assert number_of_substrings("abc") == 6
    assert number_of_substrings("abca") == 7
    assert number_of_substrings("abcaaa") == 9
    assert number_of_substrings("abcaaaab") == 12
    assert number_of_substrings("abcaaaabaa") == 15
    assert number_of_substrings("abcaaaabaaab") == 18
    assert number_of_substrings("abcaaaabaaabaa") == 21
    assert number_of_substrings("abcaaaabaaabaaab") == 24
    assert number_of_substrings("abcaaaabaaabaaabaa") == 27
    assert number_of_substrings("abcaaaabaaabaaabaaab") == 30
    assert number_of_substrings("abcaaaabaaabaaabaaabaa") == 33
    assert number_of_substrings("abcaaaabaaabaaabaaabaaab") == 36
    assert number_of_substrings("abcaaaabaaabaaabaaabaaabaa") == 39
    assert number_of_substrings("abcaaaabaaabaaabaaabaaabaaab") == 42
    assert number_of_substrings("abcaaaabaaabaaabaaabaaabaaabaa") == 45
    assert number_of_substrings("abcaaaabaaabaaabaaabaaabaaabaaab") == 48
    assert number_of_substrings("abcaaaabaaabaaabaaabaaabaaabaaabaa") == 51
    assert number_of_substrings("abcaaaabaaabaaabaaabaaabaaabaaabaaab") == 54
    assert number_of_substrings("abcaaaabaaabaaabaaabaaabaaabaaabaaabaa") == 57
    assert number_of_substrings("abcaaaabaaabaaabaaabaaabaaabaaabaaabaaab") == 60
    assert number_of_substrings("abcaaaabaaabaaabaaabaaabaaabaaabaaabaaabaa") == 63
    assert number_of_substrings("abcaaaabaaabaaabaaabaaabaaabaaabaaabaaabaaab") == 66
    assert number_of_substrings("abcaaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaa") == 69
    assert number_of_substrings("abcaaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaab") == 72
    assert number_of_substrings("abcaaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaa") == 75
    assert number_of_substrings("abcaaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaab") == 78
    assert number_of_substrings("abcaaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaa") == 81
    assert number_of_substrings("abcaaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaab") == 84
    assert number_of_substrings("abcaaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaa") == 87
    assert number_of_substrings("abcaaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaab") == 90
    assert number_of_substrings("abcaaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaaabaa") == 93
    assert number_of_substrings("