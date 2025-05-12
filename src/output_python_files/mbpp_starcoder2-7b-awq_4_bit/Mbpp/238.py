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


if __name__ == "__main__":
    assert number_of_substrings("abc") == 6
    assert number_of_substrings("aba") == 4
    assert number_of_substrings("abac") == 6
    assert number_of_substrings("abacab") == 9
    assert number_of_substrings("abacaba") == 10
    assert number_of_substrings("abacabad") == 11
    assert number_of_substrings("abacabadabacaba") == 15
    assert number_of_substrings("abacabadabacabadabacaba") == 19
    assert number_of_substrings("abacabadabacabadabacabadabacaba") == 23
    assert number_of_substrings("abacabadabacabadabacabadabacabadabacaba") == 27
    assert number_of_substrings("abacabadabacabadabacabadabacabadabacabadabacaba") == 31
    assert number_of_substrings("abacabadabacabadabacabadabacabadabacabadabacabadabacaba") == 35
    assert number_of_substrings("abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacaba") == 39
    assert number_of_substrings("abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacaba") == 43
    assert number_of_substrings("abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacaba") == 47
    assert number_of_substrings("abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacaba") == 51
    assert number_of_substrings("abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacaba") == 55
    assert number_of_substrings("abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacaba") == 59
    assert number_of_substrings("abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacaba") == 63
    assert number_of_substrings("abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacaba") == 67
    assert number_of_substrings("abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabadabacaba") == 71
    assert number_of_substrings("abacabadabacabadabacabadabacabadabacabadabacabadabacabadabacabad