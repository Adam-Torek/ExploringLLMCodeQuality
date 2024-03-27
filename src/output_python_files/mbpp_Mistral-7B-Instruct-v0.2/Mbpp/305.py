"""
Write a function to return two words from a list of words starting with letter 'p'.
assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
"""
def start_withp(words):
    p_words = [word for word in words if word.startswith('p')]
    return p_words[0], p_words[1]

assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')</s>