def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return string.lower().swapcase()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(flip_case("Hello"))
    print(flip_case("HELLO"))
    print(flip_case("hello world"))
    print(flip_case("HELLO WORLD"))