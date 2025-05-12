def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    return text == text[::-1]


def is_palindrome_recursive(text: str, start: int, end: int):
    """
    Checks if given string is a palindrome using recursion
    >>> is_palindrome_recursive('', 0, 0)
    True
    >>> is_palindrome_recursive('aba', 0, 2)
    True
    >>> is_palindrome_recursive('zbcd', 0, 3)
    False
    """
    if start >= end:
        return True
    if text[start] != text[end]:
        return False
    return is_palindrome_recursive(text, start + 1, end - 1)


def is_palindrome_recursive_with_stack(text: str):
    """
    Checks if given string is a palindrome using recursion with stack
    >>> is_palindrome_recursive_with_stack('')
    True
    >>> is_palindrome_recursive_with_stack('aba')
    True
    >>> is_palindrome_recursive_with_stack('zbcd')
    False
    """
    stack = []
    for char in text:
        stack.append(char)
    while len(stack) > 1:
        if stack.pop() != stack.pop():
            return False
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()