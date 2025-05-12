from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Initialize stack
    stack = []
    # Initialize result
    result = []
    # Iterate over string
    for char in paren_string:
        # If current character is an open parenthesis
        if char == '(':
            # Push current character onto stack
            stack.append(char)
        # If current character is a close parenthesis
        elif char == ')':
            # If stack is empty
            if not stack:
                # Append empty string to result
                result.append('')
            # Otherwise, pop top element from stack
            else:
                # Pop top element from stack
                stack.pop()
                # Append top element to result
                result.append(stack.pop())
        # If current character is not a parenthesis
        else:
            # Ignore current character
            pass
    # If stack is not empty
    if stack:
        # Append empty string to result
        result.append('')
    # Return result
    return result