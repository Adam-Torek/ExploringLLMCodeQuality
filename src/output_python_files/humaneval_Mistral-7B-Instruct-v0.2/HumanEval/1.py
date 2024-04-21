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
    index = 0
    while index < len(paren_string):
        if paren_string[index] == '(':
            stack.append(paren_string[index])
            index += 1
        elif paren_string[index] == ')':
            if not stack or stack.pop() != '(':
                raise ValueError('Invalid parentheses')
            result.append(''.join(stack))
            stack = []
            index += 1
        else:
            index += 1
    if stack:
        result.append(''.join(stack))
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()</s>