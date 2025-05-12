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
Write a function to remove duplicate characters in a string.
assert remove_duplicate("polygon") == "pogl"
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
assert reverse_string("polygon") == "gnollep"
"""
def reverse_string(string):
    new_string = ""
    for char in string:
        new_string = char + new_string
    return new_string

print(reverse_string("polygon"))

"""
Write a function to reverse a string without using the reverse function.
assert reverse_string_without_reverse("polygon") == "gnollep"
"""
def reverse_string_without_reverse(string):
    new_string = ""
    for i in range(len(string)-1,-1,-1):
        new_string += string[i]
    return new_string

print(reverse_string_without_reverse("polygon"))

"""
Write a function to check if a string is a palindrome.
assert is_palindrome("racecar") == True
assert is_palindrome("racecar") == False
"""
def is_palindrome(string):
    return string == reverse_string(string)

print(is_palindrome("racecar"))
print(is_palindrome("racecar"))

"""
Write a function to check if a string is a palindrome without using the reverse function.
assert is_palindrome_without_reverse("racecar") == True
assert is_palindrome_without_reverse("racecar") == False
"""
def is_palindrome_without_reverse(string):
    return string == reverse_string_without_reverse(string)

print(is_palindrome_without_reverse("racecar"))
print(is_palindrome_without_reverse("racecar"))

"""
Write a function to check if a string is a palindrome without using the reverse function.
assert is_palindrome_without_reverse("racecar") == True
assert is_palindrome_without_reverse("racecar") == False
"""
def is_palindrome_without_reverse(string):
    return string == reverse_string_without_reverse(string)

print(is_palindrome_without_reverse("racecar"))
print(is_palindrome_without_reverse("racecar"))

"""
Write a function to check if a string is a palindrome without using the reverse function.
assert is_palindrome_without_reverse("racecar") == True
assert is_palindrome_without_reverse("racecar") == False
"""
def is_palindrome_without_reverse(string):
    return string == reverse_string_without_reverse(string)

print(is_palindrome_without_reverse("racecar"))
print(is_palindrome_without_reverse("racecar"))

"""
Write a function to check if a string is a palindrome without using the reverse function.
assert is_palindrome_without_reverse("racecar") == True
assert is_palindrome_without_reverse("racecar") == False
"""
def is_palindrome_without_reverse(string):
    return string == reverse_string_without_reverse(string)

print(is_palindrome_without_reverse("racecar"))
print(is_palindrome_without_reverse("racecar"))

"""
Write a function to check if a string is a palindrome without using the reverse function.
assert is_palindrome_without_reverse("racecar") == True
assert is_palindrome_without_reverse("racecar") == False
"""
def is_palindrome_without_reverse(string):
    return string == reverse_string_without_reverse(string)

print(is_palindrome_without_reverse("racecar"))
print(is_palindrome_without_reverse("racecar"))

"""
Write a function to check if a string is a palindrome without using the