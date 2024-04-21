def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """

def string_sequence_with_prefix(n: int, prefix: str) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive, with a given prefix.
    >>> string_sequence_with_prefix(0, 'a')
    'a'
    >>> string_sequence_with_prefix(5, 'b')
    'b 0 1 2 3 4'
    """

def string_sequence_with_suffix(n: int, suffix: str) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive, with a given suffix.
    >>> string_sequence_with_suffix(0, 'a')
    '0 a'
    >>> string_sequence_with_suffix(5, 'b')
    '0 1 2 3 4 b'
    """

def string_sequence_with_prefix_and_suffix(n: int, prefix: str, suffix: str) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive, with a given prefix and suffix.
    >>> string_sequence_with_prefix_and_suffix(0, 'a', 'c')
    'a c'
    >>> string_sequence_with_prefix_and_suffix(5, 'b', 'd')
    'b 0 1 2 3 4 d'
    """<|endoftext|>