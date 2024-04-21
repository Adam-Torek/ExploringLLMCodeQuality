"""
Write a function to remove odd characters in a string.
assert remove_odd("python")==("yhn")
"""
def remove_odd(string):
    return "".join([i for i in string if i not in "02468"])

print(remove_odd("python"))

"""
Write a function to remove even characters in a string.
assert remove_even("python")==("pto")
"""
def remove_even(string):
    return "".join([i for i in string if i not in "13579"])

print(remove_even("python"))

"""
Write a function to remove all characters in a string except alphabets.
assert remove_non_alpha("python3.6$#")==("python")
"""
def remove_non_alpha(string):
    return "".join([i for i in string if i.isalpha()])

print(remove_non_alpha("python3.6$#"))

"""
Write a function to remove all characters in a string except digits.
assert remove_non_digit("python3.6$#")==("36")
"""
def remove_non_digit(string):
    return "".join([i for i in string if i.isdigit()])

print(remove_non_digit("python3.6$#"))

"""
Write a function to remove all characters in a string except alphabets and digits.
assert remove_non_alnum("python3.6$#")==("python36")
"""
def remove_non_alnum(string):
    return "".join([i for i in string if i.isalnum()])

print(remove_non_alnum("python3.6$#"))

"""
Write a function to remove all characters in a string except spaces.
assert remove_non_space("python3.6$#")==("python3.6$#")
"""
def remove_non_space(string):
    return "".join([i for i in string if i.isspace()])

print(remove_non_space("python3.6$#"))

"""
Write a function to remove all characters in a string except special characters.
assert remove_non_special("python3.6$#")==("$#")
"""
def remove_non_special(string):
    return "".join([i for i in string if not i.isalnum() and not i.isspace()])

print(remove_non_special("python3.6$#"))

"""
Write a function to remove all characters in a string except vowels.
assert remove_non_vowel("python3.6$#")==("pyt3.6$#")
"""
def remove_non_vowel(string):
    return "".join([i for i in string if i.lower() not in "aeiou"])

print(remove_non_vowel("python3.6$#"))

"""
Write a function to remove all characters in a string except consonants.
assert remove_non_consonant("python3.6$#")==("yhn3.6$#")
"""
def remove_non_consonant(string):
    return "".join([i for i in string if i.lower() not in "aeiou"])

print(remove_non_consonant("python3.6$#"))

"""
Write a function to remove all characters in a string except uppercase letters.
assert remove_non_upper("python3.6$#")==("python3.6$#")
"""
def remove_non_upper(string):
    return "".join([i for i in string if i.isupper()])

print(remove_non_upper("python3.6$#"))

"""
Write a function to remove all characters in a string except lowercase letters.
assert remove_non_lower("python3.6$#")==("PYTHON3.6$#")
"""
def remove_non_lower(string):
    return "".join([i for i in string if i.islower()])

print(remove_non_lower("python3.6$#"))

"""
Write a function to remove all characters in a string except alphabets and digits.
assert remove_non_alnum("python3.6$#")==("python36")
"""
def remove_non_alnum(string):
    return "".join([i for i in string if i.isalnum()])

print(remove_non_alnum("python3.6$#"))

"""