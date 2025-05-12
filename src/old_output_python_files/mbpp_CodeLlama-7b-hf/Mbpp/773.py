"""
Write a function to find the occurrence and position of the substrings within a string. Return None if there is no match.
assert occurance_substring('python programming, python language','python')==('python', 0, 6)
"""


def occurance_substring(string, substring):
    """
    :param string: string to search
    :param substring: substring to search
    :return: tuple of (substring, position, length)
    """
    if substring in string:
        return substring, string.index(substring), len(substring)
    else:
        return None


if __name__ == '__main__':
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'programming'))
    print(occurance_substring('python programming, python language', 'language'))
    print(occurance_substring('python programming, python language', 'java'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language', 'python programming, python language'))
    print(occurance_substring('python programming, python language',