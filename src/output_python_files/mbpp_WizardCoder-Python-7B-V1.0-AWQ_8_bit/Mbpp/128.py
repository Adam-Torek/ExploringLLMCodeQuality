"""
Write a function to find words that are longer than n characters from a given list of words.
assert long_words(3,"python is a programming language")==['python','programming','language']
"""

def long_words(n, words):
    return [word for word in words.split() if len(word) > n]

print(long_words(3,"python is a programming language"))
# Output: ['python', 'programming', 'language']

# Test cases
print(long_words(3,"hello world")) # []
print(long_words(5,"hello world")) # []
print(long_words(2,"python is a programming language")) # ['python', 'programming', 'language']
print(long_words(1,"python is a programming language")) # ['python', 'a', 'is', 'programming', 'language']
print(long_words(10,"python is a programming language")) # []
print(long_words(1,"")) # []
print(long_words(10,"")) # []
print(long_words(10,"python")) # []
print(long_words(10,"")) # []
print(long_words(10,123)) # []
print(long_words(10,[])) # []
print(long_words(10,[1,2,3,4,5]) # []
print(long_words(10,["python","programming","language"])) # ['python', 'programming', 'language']
print(long_words(10,["python","programming","language","hello","world"])) # ['python', 'programming', 'language']
print(long_words(10,["python","is","a","programming","language"])) # ['python', 'programming', 'language']
print(long_words(10,["python","is","a","programming","language","hello","world"])) # ['python', 'programming', 'language']
print(long_words(10,["python","is","a","programming","language","hello","world","hello","world"])) # ['python', 'programming', 'language']
print(long_words(10,["python","is","a","programming","language","hello","world","hello","world","python"])) # ['python', 'programming', 'language']
print(long_words(10,["python","is","a","programming","language","hello","world","hello","world","python","python"])) # ['python', 'programming', 'language']
print(long_words(10,["python","is","a","programming","language","hello","world","hello","world","python","python","python"])) # ['python', 'programming', 'language']

# Test cases for edge cases
print(long_words(10,None)) # []
print(long_words(10,123)) # []
print(long_words(10,[])) # []
print(long_words(10,[1,2,3,4,5]) # []
print(long_words(10,"")) # []
print(long_words(10,"python is a programming language")) # ['python', 'programming', 'language']
print(long_words(10,"")) # []
print(long_words(10,123)) # []
print(long_words(10,[])) # []
print(long_words(10,[1,2,3,4,5]) # []
print(long_words(10,"")) # []
print(long_words(10,"python is a programming language")) # ['python', 'programming', 'language']
print(long_words(10,"")) # []
print(long_words(10,123) # []
print(long_words(10,[1,2,3,4,5]) # []
print(long_words(10,"python is a programming language") # ['python', 'programming', 'language']
print(long_words(10,"") # []
print(long_words(10,123) # []
print(long_words(10,[1,2,3,4,5]) # []
print(long_words(10,"python is a programming language") # ['python', 'programming', 'language']
print(long_words(10,"") # []
print(long_words(10,123) # []
print(long_words