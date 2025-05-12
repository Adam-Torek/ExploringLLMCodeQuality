"""
Write a function to reverse words seperated by spaces in a given string.
assert reverse_words("python program")==("program python")
"""
def reverse_words(s):
    words = s.split()
    words.reverse()
    return " ".join(words)

# Test the function
assert reverse_words("python program") == "program python"<|endoftext|>