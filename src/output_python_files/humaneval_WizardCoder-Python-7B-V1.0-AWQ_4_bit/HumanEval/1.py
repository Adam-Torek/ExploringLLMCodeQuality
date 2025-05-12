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
            if not stack:
                return []
            if not current_group:
                current_group = '('
            stack.pop()
            if not stack:
                result.append(current_group + ')')
                current_group = ''
        else:
            current_group += char
    if stack:
        return []
    return result

def count_valid_groups(paren_string: str) -> int:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    count the number of valid groups in the string. A group is valid if it is properly balanced and not nested within
    any other group.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> count_valid_groups('( ) (( )) (( )( ))')
    2
    """
    groups = separate_paren_groups(paren_string)
    return len(groups)

if __name__ == "__main__":
    import doctest
    doctest.testmod()