"""
Write a function to replace characters in a string.
assert replace_char("polygon",'y','l')==("pollgon")
"""
def replace_char(string,old,new):
    new_string = ""
    for char in string:
        if char == old:
            new_string += new
        else:
            new_string += char
    return new_string

print(replace_char("polygon",'y','l'))

"""
Write a function to remove duplicate characters from a string.
assert remove_duplicate("polygon") == ("pogl")
"""
def remove_duplicate(string):
    new_string = ""
    for char in string:
        if char not in new_string:
            new_string += char
    return new_string

print(remove_duplicate("polygon"))

"""
Write a function to reverse a string.
assert reverse("polygon") == ("gnollep")
"""
def reverse(string):
    new_string = ""
    for char in string:
        new_string = char + new_string
    return new_string

print(reverse("polygon"))

"""
Write a function to check if a string is a palindrome.
assert is_palindrome("radar") == True
"""
def is_palindrome(string):
    return string == reverse(string)

print(is_palindrome("radar"))

"""
Write a function to check if a string is a palindrome.
assert is_palindrome("radar") == True
"""
def is_palindrome(string):
    return string == reverse(string)

print(is_palindrome("radar"))

"""
Write a function to check if a string is a palindrome.
assert is_palindrome("radar") == True
"""
def is_palindrome(string):
    return string == reverse(string)

print(is_palindrome("radar"))

"""
Write a function to check if a string is a palindrome.
assert is_palindrome("radar") == True
"""
def is_palindrome(string):
    return string == reverse(string)

print(is_palindrome("radar"))

"""
Write a function to check if a string is a palindrome.
assert is_palindrome("radar") == True
"""
def is_palindrome(string):
    return string == reverse(string)

print(is_palindrome("radar"))

"""
Write a function to check if a string is a palindrome.
assert is_palindrome("radar") == True
"""
def is_palindrome(string):
    return string == reverse(string)

print(is_palindrome("radar"))

"""
Write a function to check if a string is a palindrome.
assert is_palindrome("radar") == True
"""
def is_palindrome(string):
    return string == reverse(string)

print(is_palindrome("radar"))

"""
Write a function to check if a string is a palindrome.
assert is_palindrome("radar") == True
"""
def is_palindrome(string):
    return string == reverse(string)

print(is_palindrome("radar"))

"""
Write a function to check if a string is a palindrome.
assert is_palindrome("radar") == True
"""
def is_palindrome(string):
    return string == reverse(string)

print(is_palindrome("radar"))

"""
Write a function to check if a string is a palindrome.
assert is_palindrome("radar") == True
"""
def is_palindrome(string):
    return string == reverse(string)

print(is_palindrome("radar"))

"""
Write a function to check if a string is a palindrome.
assert is_palindrome("radar") == True
"""
def is_palindrome(string):
    return string == reverse(string)

print(is_palindrome("radar"))

"""
Write a function to check if a string is a palindrome.
assert is_palindrome("radar") == True
"""
def is_palindrome(string):
    return string == reverse(string)

print(is_palindrome("radar"))

"""
Write a function to check if a string is a palindrome.
assert is_palindrome("radar") == True
"""
def is_palindrome(string):
    return string == reverse(string)

print(is_pal