"""
Write a function to return two words from a list of words starting with letter 'p'.
assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
"""

def start_withp(words):
    p_words = []
    for word in words:
        if word.startswith('p'):
            p_words.append(word.split()[0])
    return tuple(p_words)

print(start_withp(["Python PHP", "Java JavaScript", "c c++"])) # ('Python', 'PHP')
print(start_withp(["Python", "Java", "JavaScript", "c"])) # ('Python', 'Java')
print(start_withp(["Python", "Java", "JavaScript", "c++"])) # ('Python', 'Java')
print(start_withp(["Python", "Java", "JavaScript", "c++", "Python"])) # ('Python', 'Java')
print(start_withp(["Python", "Java", "JavaScript", "c"])) # ('Python', 'Java')
print(start_withp(["Python", "Java", "JavaScript", "c++", "Python", "Java"])) # ('Python', 'Java')
print(start_withp(["Python", "Java", "JavaScript", "c++", "Python", "Java", "Python"])) # ('Python', 'Java')
print(start_withp(["Python", "Java", "JavaScript", "c++", "Python", "Java", "Python", "Java"])) # ('Python', 'Java')
print(start_withp(["Python", "Java", "JavaScript", "c++", "Python", "Java", "Python", "Java", "Python"])) # ('Python', 'Java')
print(start_withp(["Python", "Java", "JavaScript", "c++", "Python", "Java", "Python", "Java", "Python", "Python"])) # ('Python', 'Java')
print(start_withp(["Python", "Java", "JavaScript", "c++", "Python", "Java", "Python", "Java", "Python", "Python", "Python"])) # ('Python', 'Java')
print(start_withp(["Python", "Java", "JavaScript", "c++", "Python", "Java", "Python", "Java", "Python", "Python", "Python", "Python"])) # ('Python', 'Java')
print(start_withp(["Python", "Java", "JavaScript", "c++", "Python", "Java", "Python", "Java", "Python", "Python", "Python", "Python", "Python"])) # ('Python', 'Java')
print(start_withp(["Python", "Java", "JavaScript", "c++", "Python", "Java", "Python", "Java", "Python", "Python", "Python", "Python", "Python", "Python"])) # ('Python', 'Java')
print(start_withp(["Python", "Java", "JavaScript", "c++", "Python", "Java", "Python", "Java", "Python", "Python", "Python", "Python", "Python", "Python", "Python"])) # ('Python', 'Java')
print(start_withp(["Python", "Java", "JavaScript", "c++", "Python", "Java", "Python", "Java", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python"])) # ('Python', 'Java')
print(start_withp(["Python", "Java", "JavaScript", "c++", "Python", "Java", "Python", "Java", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python"])) # ('Python', 'Java')
print(start_withp(["Python", "Java", "JavaScript", "c++", "Python", "Java", "Python", "Java", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python"])) # ('Python', 'Java')
print(start_withp(["Python", "Java", "JavaScript", "c++", "Python", "Java", "Python", "Java", "Python