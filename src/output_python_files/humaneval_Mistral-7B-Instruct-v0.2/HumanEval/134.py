def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
    if txt:
        last_char = txt[-1]
        if last_char.isalpha() and not txt[-1].isalnum():
            return True
        else:
            return False
    else:
        return False

# Test cases
print(check_if_last_char_is_a_letter("apple pie")) # False
print(check_if_last_char_is_a_letter("apple pi e")) # True
print(check_if_last_char_is_a_letter("apple pi e ")) # False
print(check_if_last_char_is_a_letter("")) # False
print(check_if_last_char_is_a_letter("hello world")) # False
print(check_if_last_char_is_a_letter("hello world ")) # False
print(check_if_last_char_is_a_letter("hello world !")) # False
print(check_if_last_char_is_a_letter("hello world ! ")) # False
print(check_if_last_char_is_a_letter("hello world ! !")) # False
print(check_if_last_char_is_a_letter("hello world ! ! ")) # False
print(check_if_last_char_is_a_letter("hello world ! ! ")) # False
print(check_if_last_char_is_a_letter("hello world ! ! ")) # False
print(check_if_last_char_is_a_letter("hello world ! ! ")) # False
print(check_if_last_char_is_a_letter("hello world ! ! ")) # False
print(check_if_last_char_is_a_letter("hello world ! ! ")) # False
print(check_if_last_char_is_a_letter("hello world ! ! ")) # False
print(check_if_last_char_is_a_letter("hello world ! ! ")) # False
print(check_if_last_char_is_a_letter("hello world ! ! ")) # False
print(check_if_last_char_is_a_letter("hello world ! ! ")) # False
print(check_if_last_char_is_a_letter("hello world ! ! ")) # False
print(check_if_last_char_is_a_letter("hello world ! ! ")) # False
print(check_if_last_char_is_a_letter("hello world ! ! ")) # False
print(check_if_last_char_is_a_letter("hello world ! ! ")) # False
print(check_if_last_char_is_a_letter("hello world ! ! ")) # False
print(check_if_last_char_is_a_letter("hello world ! ! ")) # False
print(check_if_last_char_is_a_letter("hello world ! ! ")) # False
print(check_if_last_char_is_a_letter("hello world ! ! ")) # False
print(check_if_last_char_is_a_letter("hello world ! ! ")) # False
print(check_if_last_char_is_a_letter("hello world ! ! ")) # False
print(check_if_last_char_is_a_letter("hello world ! ! ")) # False
print(check_if_last_char_is_a_letter("hello world ! ! ")) # False
print(check_if_last_char_is_a_letter("hello world ! ! ")) # False