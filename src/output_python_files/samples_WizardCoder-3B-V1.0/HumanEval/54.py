def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """

def same_chars_count(s0: str, s1: str):
    """
    Count the number of characters that are the same in two words.
    >>> same_chars_count('eabcdzzzz', 'dddzzzzzzzddeddabc')
    10
    >>> same_chars_count('abcd', 'dddddddabc')
    0
    >>> same_chars_count('dddddddabc', 'abcd')
    0
    >>> same_chars_count('eabcd', 'dddddddabc')
    0
    >>> same_chars_count('abcd', 'dddddddabce')
    0
    >>> same_chars_count('eabcdzzzz', 'dddzzzzzzzddddabc')
    0
    """
    count = 0
    for i in range(min(len(s0), len(s1))):
        if s0[i] == s1[i]:
            count += 1
    return count

def same_chars_percentage(s0: str, s1: str):
    """
    Calculate the percentage of characters that are the same in two words.
    >>> same_chars_percentage('eabcdzzzz', 'dddzzzzzzzddeddabc')
    0.5
    >>> same_chars_percentage('abcd', 'dddddddabc')
    0.0
    >>> same_chars_percentage('dddddddabc', 'abcd')
    0.0
    >>> same_chars_percentage('eabcd', 'dddddddabc')
    0.0
    >>> same_chars_percentage('abcd', 'dddddddabce')
    0.0
    >>> same_chars_percentage('eabcdzzzz', 'dddzzzzzzzddddabc')
    0.0
    """
    count = same_chars_count(s0, s1)
    total = min(len(s0), len(s1))
    return count / total if total > 0 else 0

def main():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    main()<|endoftext|>