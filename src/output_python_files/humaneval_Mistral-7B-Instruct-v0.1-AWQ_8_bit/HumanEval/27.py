def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(char.upper() if char.islower() else char.lower() for char in string)


def is_valid_number(string: str) -> bool:
    """ For a given string, check if it is a valid number.
    >>> is_valid_number('123')
    True
    >>> is_valid_number('123a')
    False
    """
    try:
        float(string)
        return True
    except ValueError:
        return False


def is_valid_password(string: str) -> bool:
    """ For a given string, check if it is a valid password.
    >>> is_valid_password('1234567890')
    True
    >>> is_valid_password('1234567890!')
    True
    >>> is_valid_password('123')
    False
    """
    if len(string) >= 8:
        has_digit = any(char.isdigit() for char in string)
        has_upper = any(char.isupper() for char in string)
        has_lower = any(char.islower() for char in string)
        return has_digit and has_upper and has_lower
    else:
        return False


def is_valid_email(string: str) -> bool:
    """ For a given string, check if it is a valid email address.
    >>> is_valid_email('user@example.com')
    True
    >>> is_valid_email('user')
    False
    >>> is_valid_email('user@example')
    False
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, string) is not None


def is_valid_url(string: str) -> bool:
    """ For a given string, check if it is a valid URL.
    >>> is_valid_url('https://www.google.com')
    True
    >>> is_valid_url('https://www.google')
    False
    >>> is_valid_url('http://www.google.com/')
    True
    """
    import re
    pattern = r'^https?://\S+$'
    return re.match(pattern, string) is not None


def is_valid_phone_number(string: str) -> bool:
    """ For a given string, check if it is a valid phone number.
    >>> is_valid_phone_number('+1 555-1234')
    True
    >>> is_valid_phone_number('555-1234')
    True
    >>> is_valid_phone_number('1234567890')
    False
    """
    import re
    pattern = r'^\+?[\d\s()-]*$'
    return re.match(pattern, string) is not None


def is_valid_date(string: str) -> bool:
    """ For a given string, check if it is a valid date.
    >>> is_valid_date('2022-01-01')
    True
    >>> is_valid_date('2022-01-02')
    True
    >>> is_valid_date('2022-01-03')
    False
    """
    import re
    pattern = r'^(0[1-9]|1[0-2])\/(0[1-9]|[12]\d|3[01])\/(19|20)\d{2}$'
    return re.match(pattern, string) is not None


def is_valid_time(string: str) -> bool:
    """ For a given string, check if it is a valid time.
    >>> is_valid_time('00:00:00')
    True