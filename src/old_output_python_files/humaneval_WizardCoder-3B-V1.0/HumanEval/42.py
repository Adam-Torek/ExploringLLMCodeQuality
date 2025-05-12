def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
#     return [x + 1 for x in l]
    return [x + 1 for x in l]

def is_palindrome(s: str) -> bool:
    """Return True if s is a palindrome, False otherwise.
    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('hello')
    False
    """
    return s == s[::-1]

def is_unique(s: str) -> bool:
    """Return True if s contains only unique characters, False otherwise.
    >>> is_unique('hello')
    True
    >>> is_unique('racecar')
    False
    """
    return len(s) == len(set(s))

def is_valid_email(email: str) -> bool:
    """Return True if email is a valid email address, False otherwise.
    >>> is_valid_email('example@example.com')
    True
    >>> is_valid_email('example@example')
    False
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def is_valid_phone_number(phone_number: str) -> bool:
    """Return True if phone_number is a valid phone number, False otherwise.
    >>> is_valid_phone_number('123-456-7890')
    True
    >>> is_valid_phone_number('123-456-789')
    False
    """
    import re
    pattern = r'^(\d{3})[-.]?(\d{3})[-.]?(\d{4})$'
    return re.match(pattern, phone_number) is not None

def is_valid_zip_code(zip_code: str) -> bool:
    """Return True if zip_code is a valid zip code, False otherwise.
    >>> is_valid_zip_code('12345')
    True
    >>> is_valid_zip_code('1234')
    False
    """
    import re
    pattern = r'^[0-9]{5}(?:[-\s]\d{4})?$'
    return re.match(pattern, zip_code) is not None

def is_valid_credit_card(credit_card: str) -> bool:
    """Return True if credit_card is a valid credit card number, False otherwise.
    >>> is_valid_credit_card('1234-5678-9012-3456')
    True
    >>> is_valid_credit_card('1234-5678-9012-345')
    False
    """
    import re
    pattern = r'^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\d{3})\d{11})$'
    return re.match(pattern, credit_card) is not None

def is_valid_ssn(ssn: str) -> bool:
    """Return True if ssn is a valid social security number, False otherwise.
    >>> is_valid_ssn('123-45-6789')
    True
    >>> is_valid_ssn('123-45-678')
    False
    """
    import re
    pattern = r'^(\d{3})[-.]?(\d{2})[-.]?(\d{4})$'
    return re.match(pattern, ssn) is not None

def is_valid_ip_address(ip_address: str) ->