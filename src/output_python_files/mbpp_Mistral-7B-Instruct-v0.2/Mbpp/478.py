"""
Write a function to remove lowercase substrings from a given string.
assert remove_lowercase("PYTHon")==('PYTH')
"""
def remove_lowercase(string):
    """
    :param string: string to remove lowercase substrings from
    :return: string with all lowercase substrings removed
    """
    return ''.join(filter(lambda x: x.isupper() or not x, string))

# Test case
assert remove_lowercase("PYTHon") == "PYTH"
assert remove_lowercase("PyThOn") == "PYTH"
assert remove_lowercase("PyThOn123") == "PYTH123"
assert remove_lowercase("PyThOn_123") == "PYTH_123"
assert remove_lowercase("PyThOn!@#$%^&*()_+-=[]{}|;:,.<>/?`~") == "PYTH!@#$%^&*()_+-=[]{}|;:,.<>/?`~"
assert remove_lowercase("PyThOn 123 456") == "PYTH 123 456"
assert remove_lowercase("PyThOn 123 456 ") == "PYTH 123 456 "
assert remove_lowercase("PyThOn 123 456 \t") == "PYTH 123 456 \t"
assert remove_lowercase("PyThOn 123 456 \t\n") == "PYTH 123 456 \t\n"
assert remove_lowercase("PyThOn 123 456 \t\n\r") == "PYTH 123 456 \t\n\r"
assert remove_lowercase("PyThOn 123 456 \t\n\r\f") == "PYTH 123 456 \t\n\r\f"
assert remove_lowercase("PyThOn 123 456 \t\n\r\f\v") == "PYTH 123 456 \t\n\r\f\v"
assert remove_lowercase("PyThOn 123 456 \t\n\r\f\v\b") == "PYTH 123 456 \t\n\r\f\v\b"
assert remove_lowercase("PyThOn 123 456 \t\n\r\f\v\b\n") == "PYTH 123 456 \t\n\r\f\v\b"
assert remove_lowercase("PyThOn 123 456 \t\n\r\f\v\b\n\t") == "PYTH 123 456 \t\n\r\f\v\b"
assert remove_lowercase("PyThOn 123 456 \t\n\r\f\v\b\n\t\r") == "PYTH 123 456 \t\n\r\f\v\b"
assert remove_lowercase("PyThOn 123 456 \t\n\r\f\v\b\n\t\r\n") == "PYTH 123 456 \t\n\r\f\v\b"
assert remove_lowercase("PyThOn 123 456 \t\n\r\f\v\b\n\t\r\n\t") == "PYTH 123 456 \t\n\r\f\v\b"
assert remove_lowercase("PyThOn 123 456 \t\n\r\f\v\b\n\t\r\n\t\r") == "PYTH 123 456 \t\n\r\f\v\b"
assert remove_lowercase("PyThOn 123 456 \t\n\r\f\v\b\n\t\r\n\t\r\n") == "PYTH 123 456 \t\n