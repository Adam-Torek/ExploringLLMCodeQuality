from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack = []
    result = []
    current_group = ''
    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
                current_group += char
            else:
                result.append(current_group)
                current_group = ''
        else:
            current_group += char
    if current_group:
        result.append(current_group)
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()