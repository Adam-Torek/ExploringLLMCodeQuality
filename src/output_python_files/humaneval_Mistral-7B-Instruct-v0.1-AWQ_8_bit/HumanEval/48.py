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
    text = text.lower()
    text = ''.join(c for c in text if c.isalnum())
    return text == text[::-1]


def main():
    """
    Main function
    """
    print(is_palindrome(''))
    print(is_palindrome('aba'))
    print(is_palindrome('aaaaa'))
    print(is_palindrome('zbcd'))


if __name__ == '__main__':
    main()