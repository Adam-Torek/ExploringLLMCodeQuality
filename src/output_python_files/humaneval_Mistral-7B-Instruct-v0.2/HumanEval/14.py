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
    >>> common_prefix(['flower', 'flow', 'flight'])
    'fl'
    """
    if not strings:
        return ""
    return strings[0][:min(len(s) for s in strings)]


def common_suffix(strings: List[str]) -> str:
    """ Return the longest common suffix of the given strings
    >>> common_suffix(['flower', 'flow', 'flight'])
    'er'
    """
    if not strings:
        return ""
    return strings[-1][:len(strings[-1]) - (len(strings[-1]) - len(strings[0]))]


def longest_common_substring(strings: List[str]) -> str:
    """ Return the longest common substring of the given strings
    >>> longest_common_substring(['flower', 'flow', 'flight'])
    'fl'
    """
    if not strings:
        return ""
    prefixes = [all_prefixes(s) for s in strings]
    common_prefixes = [common_prefix(p) for p in zip(prefixes, *[all_prefixes(s)[1:] for s in strings[1:]])]
    return next((cp for cp in common_prefixes if len(cp) > len(common_prefix(common_prefixes))), "")


if __name__ == "__main__":
    import doctest
    doctest.testmod()</s>