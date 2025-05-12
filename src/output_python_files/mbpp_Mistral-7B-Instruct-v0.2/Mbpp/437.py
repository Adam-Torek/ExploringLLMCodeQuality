"""
Write a function to remove odd characters in a string.
assert remove_odd("python")==("yhn")
"""
def remove_odd(string):
    """
    Function to remove odd indexed characters from a string
    :param string: string to be processed
    :return: string with odd indexed characters removed
    """
    return ''.join([char for index, char in enumerate(string) if index % 2 == 0])

assert remove_odd("python") == "yhn"
assert remove_odd("hello") == "l"
assert remove_odd("") == ""
assert remove_odd("abcd") == ""
assert remove_odd("12345") == ""
assert remove_odd("123456") == "246"
assert remove_odd("1234567") == "246"
assert remove_odd("12345678") == "246"
assert remove_odd("123456789") == "2468"
assert remove_odd("1234567890") == "2468"
assert remove_odd("12345678901") == "246801"
assert remove_odd("123456789012") == "2468012"
assert remove_odd("1234567890123") == "24680123"
assert remove_odd("12345678901234") == "246801234"
assert remove_odd("123456789012345") == "2468012345"
assert remove_odd("1234567890123456") == "24680123456"
assert remove_odd("12345678901234567") == "246801234567"
assert remove_odd("123456789012345678") == "2468012345678"
assert remove_odd("1234567890123456789") == "24680123456789"
assert remove_odd("12345678901234567890") == "246801234567890"
assert remove_odd("123456789012345678901") == "2468012345678901"
assert remove_odd("1234567890123456789012") == "24680123456789012"
assert remove_odd("12345678901234567890123") == "246801234567890123"
assert remove_odd("123456789012345678901234") == "2468012345678901234"
assert remove_odd("1234567890123456789012345") == "24680123456789012345"
assert remove_odd("12345678901234567890123456") == "246801234567890123456"
assert remove_odd("123456789012345678901234567") == "2468012345678901234567"