"""
Write a function to return two words from a list of words starting with letter 'p'.
assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
"""

def start_withp(lst):
    """
    Function to return two words from a list of words starting with letter 'p'
    """
    p_words = []
    for word in lst:
        if word[0] == 'p':
            p_words.append(word)
    if len(p_words) < 2:
        return None
    else:
        return p_words[0], p_words[1]

# Testing the function
assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
assert start_withp(["Python", "Java", "c"])==('Python', 'Java')
assert start_withp(["Python", "Java", "c", "Python"])==('Python', 'Java')