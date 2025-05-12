"""
Write a function to reverse words seperated by spaces in a given string.
assert reverse_words("python program")==("program python")
"""

def reverse_words(string):
    words = string.split()
    words.reverse()
    return " ".join(words)

print(reverse_words("python program")) # Output: "program python"
print(reverse_words("hello world")) # Output: "world hello"
print(reverse_words("i am a student")) # Output: "student a am i"
print(reverse_words("geeks for geeks")) # Output: "geeks for geeks"