from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # TODO: Implement this function
    return []


def is_balanced(paren_string: str) -> bool:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    determine if the parentheses are balanced.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> is_balanced('( ) (( )) (( )( ))')
    True
    >>> is_balanced('( ) (( )) (( )( )')
    False
    """
    # TODO: Implement this function
    return False


def is_nested(paren_string: str) -> bool:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    determine if the parentheses are nested.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> is_nested('( ) (( )) (( )( ))')
    False
    >>> is_nested('( ) (( )) (( )( )')
    True
    """
    # TODO: Implement this function
    return False


def is_valid(paren_string: str) -> bool:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    determine if the parentheses are valid.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> is_valid('( ) (( )) (( )( ))')
    True
    >>> is_valid('( ) (( )) (( )( )')
    False
    """
    # TODO: Implement this function
    return False


def is_valid_with_stack(paren_string: str) -> bool:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    determine if the parentheses are valid.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> is_valid_with_stack('( ) (( )) (( )( ))')
    True
    >>> is_valid_with_stack('( ) (( )) (( )( )')
    False
    """
    # TODO: Implement this function
    return False


def is_valid_with_stack_and_queue(paren_string: str) -> bool:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    determine if the parentheses are valid.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> is_valid_with_stack_and_queue('( ) (( )) (( )( ))')
    True
    >>> is_valid_with_stack_and_queue('( ) (( )) (( )( )')
    False
    """
    # TODO: Implement this function
    return False


def is_valid_with_stack_and_queue_and_set(paren_string: str) -> bool:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    determine if the parentheses are valid.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> is_valid_with_stack_and_queue_and_set('( ) (( )) (( )( ))')
    True
    >>> is_valid_