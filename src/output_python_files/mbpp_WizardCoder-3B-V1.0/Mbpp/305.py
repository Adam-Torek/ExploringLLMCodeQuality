"""
Write a function to return two words from a list of words starting with letter 'p'.
assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
"""
def start_withp(words):
    for word in words:
        if word[0] == 'p':
            return word.split()[0], word.split()[1]
    return None, None<|endoftext|>