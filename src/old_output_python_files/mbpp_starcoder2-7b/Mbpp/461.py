"""
Write a python function to count the upper case characters in a given string.
assert upper_ctr('PYthon') == 1
"""

def upper_ctr(s):
    count = 0
    for c in s:
        if c.isupper():
            count += 1
    return count

assert upper_ctr('PYthon') == 1
assert upper_ctr('Python') == 2
assert upper_ctr('python') == 0
assert upper_ctr('Python is easy') == 2
assert upper_ctr('Python is easy to learn') == 2
assert upper_ctr('Python is easy to learn and fun') == 2
assert upper_ctr('Python is easy to learn and fun.') == 2
assert upper_ctr('Python is easy to learn and fun. It is a great language.') == 2
assert upper_ctr('Python is easy to learn and fun. It is a great language. It is a great language.') == 2
assert upper_ctr('Python is easy to learn and fun. It is a great language. It is a great language. It is a great language.') == 2
assert upper_ctr('Python is easy to learn and fun. It is a great language. It is a great language. It is a great language. It is a great language.') == 2
assert upper_ctr('Python is easy to learn and fun. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language.') == 2
assert upper_ctr('Python is easy to learn and fun. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language.') == 2
assert upper_ctr('Python is easy to learn and fun. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language.') == 2
assert upper_ctr('Python is easy to learn and fun. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language.') == 2
assert upper_ctr('Python is easy to learn and fun. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language.') == 2
assert upper_ctr('Python is easy to learn and fun. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language.') == 2
assert upper_ctr('Python is easy to learn and fun. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language.') == 2
assert upper_ctr('Python is easy to learn and fun. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language.') == 2
assert upper_ctr('Python is easy to learn and fun. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language.') == 2
assert upper_ctr('Python is easy to learn and fun. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is a great language. It is