"""
Write a function to check whether the given string is starting with a vowel or not using regex.
assert check_str("annie")
"""
import re


def check_str(string):
    """
    Function to check whether the given string starts with a vowel or not using regex.
    :param string: str
    :return: bool
    """
    pattern = re.compile(r'^[aeiouAEIOU]')
    match = pattern.match(string)
    if match:
        return True
    else:
        return False


if __name__ == "__main__":
    assert check_str("annie")
    assert not check_str("bob")
    assert check_str("Ella")
    assert check_str("Alice")
    assert not check_str("Tom")
    assert not check_str("")
    assert not check_str("123")
    assert not check_str("abcd")
    assert not check_str("AbCd")
    assert not check_str("AbCdEfGhIjKlMnOpQrStUvWxYz")
    assert not check_str("AbCdEfGhIjKlMnOpQrStUvWxYz123")
    assert not check_str("AbCdEfGhIjKlMnOpQrStUvWxYz123!@#$%^&*()_+-=[]{}|;:,.<>?/")
    assert not check_str("AbCdEfGhIjKlMnOpQrStUvWxYz123!@#$%^&*()_+-=[]{}|;:,.<>?/ ")
    assert not check_str("AbCdEfGhIjKlMnOpQrStUvWxYz123!@#$%^&*()_+-=[]{}|;:,.<>?/  ")
    assert not check_str("AbCdEfGhIjKlMnOpQrStUvWxYz123!@#$%^&*()_+-=[]{}|;:,.<>?/  \t")
    assert not check_str("AbCdEfGhIjKlMnOpQrStUvWxYz123!@#$%^&*()_+-=[]{}|;:,.<>?/  \t\n")
    assert not check_str("AbCdEfGhIjKlMnOpQrStUvWxYz123!@#$%^&*()_+-=[]{}|;:,.<>?/  \t\n\r")
    assert not check_str("AbCdEfGhIjKlMnOpQrStUvWxYz123!@#$%^&*()_+-=[]{}|;:,.<>?/  \t\n\r\f")
    assert not check_str("AbCdEfGhIjKlMnOpQrStUvWxYz123!@#$%^&*()_+-=[]{}|;:,.<>?/  \t\n\r\f\v")
    assert not check_str("AbCdEfGhIjKlMnOpQrStUvWxYz123!@#$%^&*()_+-=[]{}|;:,.<>?/  \t\n\r\f\v\b")
    assert not check_str("AbCdEfGhIjKlMnOpQrStUvWxYz123!@#$%^&*()_+-=[]{}|;:,.<>?/  \t\n\r\f\v\b\n")
    assert not check_str("AbCdEfGhIjKlMnOpQrStUvW