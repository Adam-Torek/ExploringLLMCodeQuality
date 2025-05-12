"""
Write a function that matches a string that has an 'a' followed by anything, ending in 'b'.
assert text_starta_endb("aabbbb")
"""

def text_starta_endb(text):
    return re.search('a.*b$', text)

"""
Write a function that matches a string that has an 'a' followed by 3 'b'.
assert text_a_b_b_b("aabbbb")
"""

def text_a_b_b_b(text):
    return re.search('a.*b.*b.*b$', text)

"""
Write a function that matches a string that has an 'a' followed by 3 'b' or 4 'c'.
assert text_a_b_b_b_or_c("aabbbb")
"""

def text_a_b_b_b_or_c(text):
    return re.search('a.*b.*b.*b|a.*b.*b.*b.*c$', text)

"""
Write a function that matches a string that has an 'a' followed by anything, ending in 'b',
but it must be at least 3 characters long.
assert text_starta_endb_min_length_3("aabbb")
"""

def text_starta_endb_min_length_3(text):
    return re.search('a.*b$', text)

"""
Write a function that matches a string that has an 'a' followed by 3 'b' or 4 'c',
but it must be at least 3 characters long.
assert text_a_b_b_b_or_c_min_length_3("aabbb")
"""

def text_a_b_b_b_or_c_min_length_3(text):
    return re.search('a.*b.*b.*b|a.*b.*b.*b.*c$', text)

"""
Write a function that matches a string that has an 'a' followed by 3 'b' or 4 'c',
but it must be at least 3 characters long.
assert text_a_b_b_b_or_c_min_length_3("aabbb")
"""

def text_a_b_b_b_or_c_min_length_3(text):
    return re.search('a.*b.*b.*b|a.*b.*b.*b.*c$', text)

"""
Write a function that matches a string that has an 'a' followed by 3 'b' or 4 'c',
but it must be at least 3 characters long.
assert text_a_b_b_b_or_c_min_length_3("aabbb")
"""

def text_a_b_b_b_or_c_min_length_3(text):
    return re.search('a.*b.*b.*b|a.*b.*b.*b.*c$', text)

"""
Write a function that matches a string that has an 'a' followed by 3 'b' or 4 'c',
but it must be at least 3 characters long.
assert text_a_b_b_b_or_c_min_length_3("aabbb")
"""

def text_a_b_b_b_or_c_min_length_3(text):
    return re.search('a.*b.*b.*b|a.*b.*b.*b.*c$', text)

"""
Write a function that matches a string that has an 'a' followed by 3 'b' or 4 'c',
but it must be at least 3 characters long.
assert text_a_b_b_b_or_c_min_length_3("aabbb")
"""

def text_a_b_b_b_or_c_min_length_3(text):
    return re.search('a.*b.*b.*b|a.*b.*b.*b.*c$', text)

"""
Write a function that matches a string that has an 'a' followed by 3 'b' or 4 'c',
but it must be at least 3 characters long.
assert text_a_b_b_b_or_c_min_length_3("aabbb")
"""

def text_a_b_b_b_or_c_min_length_3(text):
    return re.search('a.*