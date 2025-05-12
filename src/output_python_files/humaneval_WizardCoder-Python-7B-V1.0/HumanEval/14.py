from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(1, len(string) + 1)]

def common_prefix(strings: List[str]) -> str:
    """ Return the longest common prefix of the input strings
    >>> common_prefix(['abc', 'abd', 'abcd']
    'ab'
    """
    if not strings:
        return ''
    prefix = strings[0]
    for s in strings[1:]:
        while s and s[0] != prefix[0]:
            prefix = prefix[:-1]
        if not prefix:
            return ''
        for i, c in enumerate(prefix):
            if c != s[i]:
                prefix = prefix[:i]
                break
    return prefix

def longest_common_prefix(strings: List[str]) -> str:
    """ Return the longest common prefix of the input strings
    >>> longest_common_prefix(['abc', 'abd', 'abcd']
    'ab'
    """
    return common_prefix(strings)

def longest_common_suffix(strings: List[str]) -> str:
    """ Return the longest common suffix of the input strings
    >>> longest_common_suffix(['abc', 'abd', 'abcd']
    'cd'
    """
    return common_prefix(strings[::-1])[::-1]

def longest_common_substring(strings: List[str]) -> str:
    """ Return the longest common substring of the input strings
    >>> longest_common_substring(['abcd', 'abdc', 'ab']
    'ab'
    """
    if not strings:
        return ''
    if len(strings) == 1:
        return strings[0]
    if len(strings) == 2:
        return longest_common_prefix(all_prefixes(strings[0]) & all_prefixes(strings[1]))
    return longest_common_substring(strings[1:])

def longest_common_superstring(strings: List[str]) -> str:
    """ Return the longest common superstring of the input strings
    >>> longest_common_superstring(['abc', 'abd', 'abcd']
    'abcd'
    """
    if not strings:
        return ''
    if len(strings) == 1:
        return strings[0]
    if len(strings) == 2:
        return longest_common_suffix(strings[0] + strings[1])
    return longest_common_superstring(strings[1:] + [longest_common_substring(strings)])

if __name__ == "__main__":
    import doctest
    doctest.testmod()