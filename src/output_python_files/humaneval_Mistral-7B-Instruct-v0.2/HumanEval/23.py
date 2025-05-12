def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

def reverse_string(string: str) -> str:
    """ Return reversed string
    >>> reverse_string('')
    ''
    >>> reverse_string('abc')
    'cba'
    """
    return string[::-1]

def is_palindrome(string: str) -> bool:
    """ Return True if string is palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('a')
    True
    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('hello')
    False
    """
    return string == reverse_string(string)

def main():
    """ Main function
    """
    string = input("Enter a string: ")
    length = strlen(string)
    print(f"Length of '{string}' is {length}")
    if is_palindrome(string):
        print(f"'{string}' is a palindrome")
    else:
        print(f"'{string}' is not a palindrome")

if __name__ == "__main__":
    main()