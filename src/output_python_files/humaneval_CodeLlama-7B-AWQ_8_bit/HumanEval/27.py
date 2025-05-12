def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join([c.swapcase() for c in string])


def flip_case_in_place(string: str) -> None:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case_in_place('Hello')
    >>> string
    'hELLO'
    """
    for i in range(len(string)):
        if string[i].islower():
            string = string[:i] + string[i].upper() + string[i + 1:]
        elif string[i].isupper():
            string = string[:i] + string[i].lower() + string[i + 1:]
    return string


def flip_case_in_place_2(string: str) -> None:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case_in_place_2('Hello')
    >>> string
    'hELLO'
    """
    for i in range(len(string)):
        if string[i].islower():
            string = string[:i] + string[i].upper() + string[i + 1:]
        elif string[i].isupper():
            string = string[:i] + string[i].lower() + string[i + 1:]
    return string


def flip_case_in_place_3(string: str) -> None:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case_in_place_3('Hello')
    >>> string
    'hELLO'
    """
    for i in range(len(string)):
        if string[i].islower():
            string = string[:i] + string[i].upper() + string[i + 1:]
        elif string[i].isupper():
            string = string[:i] + string[i].lower() + string[i + 1:]
    return string


def flip_case_in_place_4(string: str) -> None:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case_in_place_4('Hello')
    >>> string
    'hELLO'
    """
    for i in range(len(string)):
        if string[i].islower():
            string = string[:i] + string[i].upper() + string[i + 1:]
        elif string[i].isupper():
            string = string[:i] + string[i].lower() + string[i + 1:]
    return string


def flip_case_in_place_5(string: str) -> None:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case_in_place_5('Hello')
    >>> string
    'hELLO'
    """
    for i in range(len(string)):
        if string[i].islower():
            string = string[:i] + string[i].upper() + string[i + 1:]
        elif string[i].isupper():
            string = string[:i] + string[i].lower() + string[i + 1:]
    return string


def flip_case_in_place_6(string: str) -> None:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case_in_place_6('Hello')
    >>> string
    'hELLO'
    """
    for i in range(len(string)):
        if string[i].islower():
            string = string[:i] + string[i].upper() + string[i + 1:]
        elif string[i].isupper():
            string = string[:i] + string[i].lower() + string[i + 1:]
    return string


def flip_case