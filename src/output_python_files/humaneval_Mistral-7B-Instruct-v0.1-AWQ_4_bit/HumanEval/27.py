def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(char.upper() if char.islower() else char.lower() for char in string)


def is_palindrome(string: str) -> bool:
    """ For a given string, check if it is a palindrome.
    >>> is_palindrome('racecar')
    True
    """
    return string == string[::-1]


def is_prime(number: int) -> bool:
    """ For a given number, check if it is prime.
    >>> is_prime(2)
    True
    >>> is_prime(4)
    False
    """
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def is_leap_year(year: int) -> bool:
    """ For a given year, check if it is a leap year.
    >>> is_leap_year(2020)
    True
    >>> is_leap_year(2021)
    False
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def is_valid_email(email: str) -> bool:
    """ For a given email, check if it is valid.
    >>> is_valid_email('test@example.com')
    True
    >>> is_valid_email('test')
    False
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def is_valid_password(password: str) -> bool:
    """ For a given password, check if it is valid.
    >>> is_valid_password('123456')
    False
    >>> is_valid_password('P@ssw0rd')
    True
    """
    import re
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$'
    return re.match(pattern, password) is not None


def is_valid_phone_number(phone_number: str) -> bool:
    """ For a given phone number, check if it is valid.
    >>> is_valid_phone_number('+1234567890')
    True
    >>> is_valid_phone_number('1234567890')
    False
    """
    import re
    pattern = r'^\+?[\d\s()-]*$'
    return re.match(pattern, phone_number) is not None


def is_valid_date(date_string: str) -> bool:
    """ For a given date string, check if it is valid.
    >>> is_valid_date('2022-01-01')
    True
    >>> is_valid_date('2022-02-29')
    False
    """
    import re
    pattern = r'^(0?[1-9]|1[0-2])\/(0?[1-9]|[12]\d|3[01])\/(19|20)\d{2}$'
    return re.match(pattern, date_string