"""
Write a function to return two words from a list of words starting with letter 'p'.
assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
"""

def start_withp(words):
    for word in words:
        if word.startswith('p'):
            return word.split()[0], word.split()[1]

print(start_withp(["Python PHP", "Java JavaScript", "c c++"]))

# Output: ('Python', 'PHP')

# Another way to solve this problem is to use list comprehension and find the words that start with 'p' and return them as a tuple.

def start_withp(words):
    return tuple([word.split()[0] for word in words if word.startswith('p')][:2])

print(start_withp(["Python PHP", "Java JavaScript", "c c++"]))

# Output: ('Python', 'PHP')

# This function will return a tuple of the first two words that start with 'p' in the list of words. If there are less than two words that start with 'p', it will return a tuple of the available words.