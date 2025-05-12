from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(1, len(string) + 1)]

def longest_common_prefix(strings: List[str]) -> str:
    """ Return the longest common prefix of a list of strings
    >>> longest_common_prefix(['flower', 'flow', 'flight'])
    'fl'
    """
    if not strings:
        return ''
    shortest = min(strings, key=len)
    prefixes = [p for p in all_prefixes(shortest) if all(s.startswith(p) for s in strings)]
    return prefixes[0] if prefixes else ''

def longest_common_suffix(strings: List[str]) -> str:
    """ Return the longest common suffix of a list of strings
    >>> longest_common_suffix(['dog', 'doggy', 'dogg']
    'g'
    """
    if not strings:
        return ''
    shortest = min(strings, key=len)
    suffixes = [shortest[i:] for i in range(len(shortest) + 1)]
    common = longest_common_prefix(suffixes)
    return common if common else ''

def longest_common_subsequence(strings: List[str]) -> str:
    """ Return the longest common subsequence of a list of strings
    >>> longest_common_subsequence(['ABCDGH', 'AEDFHR', 'BEHHR', 'CDEFR'])
    'BH'
    """
    if not strings:
        return ''
    shortest = min(strings, key=len)
    subsequence = ''
    for i in range(len(shortest)):
        for string in strings:
            if shortest[i] in string:
                subsequence += shortest[i]
                break
    return subsequence

def longest_common_supersequence(strings: List[str]) -> str:
    """ Return the longest common supersequence of a list of strings
    >>> longest_common_supersequence(['ABCDGH', 'AEDFHR', 'BEHHR', 'CDEFR'])
    'ABCDGH'
    """
    if not strings:
        return ''
    shortest = min(strings, key=len)
    supersequence = ''
    for i in range(len(shortest)):
        for string in strings:
            if shortest[i] in string:
                supersequence += shortest[i]
                break
    return supersequence

if __name__ == "__main__":
    import doctest
    doctest.testmod()