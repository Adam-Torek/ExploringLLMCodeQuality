"""
Write a function to return two words from a list of words starting with letter 'p'.
assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
"""
def start_withp(words):
    return [word for word in words if word.startswith('p')]

assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')

"""
Write a function to return two words from a list of words ending with letter 'p'.
assert end_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
"""
def end_withp(words):
    return [word for word in words if word.endswith('p')]

assert end_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')

"""
Write a function to return two words from a list of words containing letter 'p'.
assert contain_p(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
"""
def contain_p(words):
    return [word for word in words if 'p' in word]

assert contain_p(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')

"""
Write a function to return two words from a list of words containing letter 'p' and 'h'.
assert contain_ph(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
"""
def contain_ph(words):
    return [word for word in words if 'p' in word and 'h' in word]

assert contain_ph(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')

"""
Write a function to return two words from a list of words containing letter 'p' and 'h' and 'j'.
assert contain_phj(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
"""
def contain_phj(words):
    return [word for word in words if 'p' in word and 'h' in word and 'j' in word]

assert contain_phj(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')

"""
Write a function to return two words from a list of words containing letter 'p' and 'h' and 'j' and's'.
assert contain_phjs(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
"""
def contain_phjs(words):
    return [word for word in words if 'p' in word and 'h' in word and 'j' in word and's' in word]

assert contain_phjs(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')

"""
Write a function to return two words from a list of words containing letter 'p' and 'h' and 'j' and's' and 't'.
assert contain_phjst(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
"""
def contain_phjst(words):
    return [word for word in words if 'p' in word and 'h' in word and 'j' in word and's' in word and 't' in word]

assert contain_phjst(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')

"""
Write a function to return two words from a list of words containing letter 'p' and 'h' and 'j' and's' and 't' and 'o'.
assert contain_phjsto(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
"""
def contain_phjsto(words):
    return [word for word in words if 'p' in word and 'h' in word and 'j' in word and's' in word and 't' in word and 'o' in word]

assert contain_phjsto(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')

"""
Write a function to return two words from a list of words containing letter 'p' and 'h' and 'j' and's'