def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return string.lower().capitalize() if string else ""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(flip_case("Hello"))
    print(flip_case("HELLO"))
    print(flip_case(""))
    print(flip_case("12345"))
    print(flip_case("12345_"))
    print(flip_case("12345_ABC"))
    print(flip_case("12345_ABC_123"))
    print(flip_case("12345_ABC_123_456"))
    print(flip_case("12345_ABC_123_456_789"))
    print(flip_case("12345_ABC_123_456_789_012"))
    print(flip_case("12345_ABC_123_456_789_012_345"))
    print(flip_case("12345_ABC_123_456_789_012_345_678"))
    print(flip_case("12345_ABC_123_456_789_012_345_678_901"))
    print(flip_case("12345_ABC_123_456_789_012_345_678_901_234"))
    print(flip_case("12345_ABC_123_456_789_012_345_678_901_234_567"))
    print(flip_case("12345_ABC_123_456_789_012_345_678_901_234_567_890"))
    print(flip_case("12345_ABC_123_456_789_012_345_678_901_234_567_890_123"))
    print(flip_case("12345_ABC_123_456_789_012_345_678_901_234_567_890_123_456"))
    print(flip_case("12345_ABC_123_456_789_012_345_678_901_234_567_890_123_456_789"))
    print(flip_case("12345_ABC_123_456_789_012_345_678_901_234_567_890_123_456_789_012"))
    print(flip_case("12345_ABC_123_456_789_012_345_678_901_234_567_890_123_456_789_012_345"))
    print(flip_case("12345_ABC_123_456_789_012_345_678_901_234_567_890_123_456_789_012_345_678"))
    print(flip_case("12