def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """

def string_sequence_with_step(n: int, step: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive with step.
    >>> string_sequence_with_step(0, 1)
    '0'
    >>> string_sequence_with_step(5, 1)
    '0 1 2 3 4 5'
    >>> string_sequence_with_step(5, 2)
    '0 2 4 5'
    """

def string_sequence_with_step_and_start(n: int, step: int, start: int) -> str:
    """ Return a string containing space-delimited numbers starting from start upto n inclusive with step.
    >>> string_sequence_with_step_and_start(0, 1, 0)
    '0'
    >>> string_sequence_with_step_and_start(5, 1, 0)
    '0 1 2 3 4 5'
    >>> string_sequence_with_step_and_start(5, 2, 0)
    '0 2 4 5'
    >>> string_sequence_with_step_and_start(5, 2, 1)
    '1 3 5'
    """

def string_sequence_with_step_and_start_and_end(start: int, end: int, step: int) -> str:
    """ Return a string containing space-delimited numbers starting from start upto end inclusive with step.
    >>> string_sequence_with_step_and_start_and_end(0, 5, 1)
    '0 1 2 3 4 5'
    >>> string_sequence_with_step_and_start_and_end(0, 5, 2)
    '0 2 4 5'
    >>> string_sequence_with_step_and_start_and_end(1, 5, 2)
    '1 3 5'
    """

def string_sequence_with_step_and_start_and_end_and_separator(start: int, end: int, step: int, separator: str) -> str:
    """ Return a string containing space-delimited numbers starting from start upto end inclusive with step.
    >>> string_sequence_with_step_and_start_and_end_and_separator(0, 5, 1, ',')
    '0,1,2,3,4,5'
    >>> string_sequence_with_step_and_start_and_end_and_separator(0, 5, 2, ',')
    '0,2,4,5'
    >>> string_sequence_with_step_and_start_and_end_and_separator(1, 5, 2, ',')
    '1,3,5'
    """

def string_sequence_with_step_and_start_and_end_and_separator_and_prefix(start: int, end: int, step: int, separator: str, prefix: str) -> str:
    """ Return a string containing space-delimited numbers starting from start upto end inclusive with step.
    >>> string_sequence_with_step_and_start_and_end_and_separator_and_prefix(0, 5, 1, ',', 'prefix')
    'prefix 0,1,2,3,4,5'
    >>> string_sequence_with_step_and_start_and_end_and_separator_and_prefix(0, 5, 2, ',', 'prefix')
    'prefix 0,2,4,5'
    >>> string_sequence_with_step_and_start_and_end_and_separator_and_prefix(1, 5, 2, ',', 'prefix')
    'prefix 1,3,5'
    """

def string_sequence_with_step_and_start_and_end_and_separator_and_prefix_and_suffix(start: int, end: int, step: int