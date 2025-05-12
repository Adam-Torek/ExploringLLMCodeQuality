from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return list(range(len(string) + 1))[1:] + [string]


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes('abc')
    ['c', 'bc', 'ab']
    """
    return list(reversed(all_prefixes(string)[::-1]))


def common_prefix(strings: List[str]) -> str:
    """ Return the longest common prefix of the given strings
    >>> common_prefix(['flower', 'flow'])
    'flow'
    """
    if not strings:
        return ""
    common = strings[0]
    for string in strings[1:]:
        while len(common) > 0 and common[-1] != string[-1]:
            common = common[:-1]
    return common


def common_suffix(strings: List[str]) -> str:
    """ Return the longest common suffix of the given strings
    >>> common_suffix(['flower', 'flow'])
    'er'
    """
    if not strings:
        return ""
    common = strings[-1]
    for string in strings[:-1]:
        while len(common) > 0 and common[-1] != string[-1]:
            common = common[:-1]
    return common


def longest_common_substring(strings: List[str]) -> str:
    """ Return the longest common substring between the given strings
    >>> longest_common_substring(['flower', 'flow'])
    'ower'
    """
    if not strings:
        return ""
    m = len(strings[0])
    n = len(strings[1])
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    longest = ""
    i, j = 0, 0
    while i < m and j < n:
        if strings[0][i] == strings[1][j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
            if dp[i + 1][j + 1] > len(longest):
                longest = strings[0][i : i + dp[i + 1][j + 1]]
            i += 1
            j += 1
        elif dp[i][j] > 0:
            i += 1
        else:
            j += 1
    return longest


if __name__ == "__main__":
    import doctest

    doctest.testmod()