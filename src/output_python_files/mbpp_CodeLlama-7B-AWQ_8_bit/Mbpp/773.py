"""
Write a function to find the occurrence and position of the substrings within a string. Return None if there is no match.
assert occurance_substring('python programming, python language','python')==('python', 0, 6)
"""


def occurance_substring(string, substring):
    """
    Write a function to find the occurrence and position of the substrings within a string. Return None if there is no match.
    """
    if substring in string:
        return substring, string.index(substring), string.index(substring) + len(substring)
    else:
        return None


if __name__ == '__main__':
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', 'python'))
    print(occurance_substring('python programming, python language', '