"""
Write a function to replace characters in a string.
assert replace_char("polygon",'y','l')==("pollgon")
"""
def replace_char(string, char_to_replace, new_char):
    """
    Replace all occurrences of char_to_replace with new_char in string
    :param string: str
    :param char_to_replace: str
    :param new_char: str
    :return: str
    """
    return string.replace(char_to_replace, new_char)

assert replace_char("polygon",'y','l')==("pollgon")
assert replace_char("hello",'l','o')==("heooo")
assert replace_char("python",'t','h')==("pyhthon")
assert replace_char("",'a','z')==("")
assert replace_char("12345",'5','x')==("1234x")
assert replace_char("12345",'5','')==("1234")
assert replace_char("12345",'5','5')==("12345")
assert replace_char("12345",'5','55')==("123455")
assert replace_char("12345",'5','555')==("123455555")
assert replace_char("12345",'5','55555')==("12345555555")
assert replace_char("12345",'5','5555555')==("1234555555555")
assert replace_char("12345",'5','555555555')==("123455555555555")
assert replace_char("12345",'5','5555555555')==("1234555555555555")
assert replace_char("12345",'5','55555555555')==("12345555555555555")
assert replace_char("12345",'5','555555555555')==("123455555555555555")
assert replace_char("12345",'5','5555555555555')==("1234555555555555555")
assert replace_char("12345",'5','55555555555555')==("12345555555555555555")
assert replace_char("12345",'5','555555555555555')==("123455555555555555555")
assert replace_char("12345",'5','5555555555555555')==("1234555555555555555555")
assert replace_char("12345",'5','55555555555555555')==("12345555555555555555555")
assert replace_char("12345",'5','555555555555555555')==("123455555555555555555555")
assert replace_char("12345",'5','5555555555555555555')==("1234555555555555555555555")