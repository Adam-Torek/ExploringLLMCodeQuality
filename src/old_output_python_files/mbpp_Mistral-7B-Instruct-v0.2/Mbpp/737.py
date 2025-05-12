"""
Write a function to check whether the given string is starting with a vowel or not using regex.
assert check_str("annie")
"""
import re

def check_str(string):
    """
    Check if the given string starts with a vowel using regex.

    :param string: str
    :return: bool
    """
    vowels = "aeiouAEIOU"
    pattern = re.compile(r"^[{}]".format(vowels))
    return bool(pattern.match(string))